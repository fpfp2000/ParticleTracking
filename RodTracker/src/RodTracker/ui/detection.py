#  Copyright (c) 2023 Adrian Niemann Dmitry Puzyrev
#
#  This file is part of RodTracker.
#  RodTracker is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  RodTracker is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with RodTracker.  If not, see <http://www.gnu.org/licenses/>.

"""**TBD**"""

import os
import sys
import logging
from typing import List
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import RodTracker.backend.logger as lg
import RodTracker.ui.mainwindow_layout as mw_l
from RodTracker.backend.img_data import ImageData

_logger = logging.getLogger(__name__)
if sys.version_info < (3, 10):
    _logger.warning("3D reconstruction is not available. "
                    "Please upgrade to Python 3.10 or greater and "
                    "reinstall the application.")
else:
    import torch
    import ParticleDetection.utils.datasets as ds
    from RodTracker.backend.detection import Detector, RodDetection
    # Don't remove the following imports, see GitHub issue as reference
    # https://github.com/pytorch/pytorch/issues/48932#issuecomment-803957396
    import cv2                                                  # noqa: F401
    import torchvision                                          # noqa: F401
    import ParticleDetection                                    # noqa: F401


def init_detection(ui: mw_l.Ui_MainWindow, image_managers: List[ImageData]):
    """Initialize the functionality of detecting particles.

    Parameters
    ----------
    ui : Ui_MainWindow
        UI object of the main window of the application, i.e. also containing
        the UI tab/objects for detection tasks.
    image_managers : List[ImageData]
        List of (relevant) image data management objects providing access to
        loaded image datasets. Only images from these objects will be available
        for particle detection.

    Returns
    -------
    None | DetectorUI
        Returns ``None``, if the system requirements for particle detections
        are not met. Otherwise the ``DetectorUI`` object handling particle
        detections is returned.
    """
    if sys.version_info < (3, 10):
        ui.tab_detection.setEnabled(False)
        return
    return DetectorUI(ui.tab_detection, image_managers)


class DetectorUI(QtWidgets.QWidget):
    """A custom ``QWidget`` to interface with a neural network for rod
    detection.

    Parameters
    ----------
    ui : QWidget
        Widget containing the tab that is the GUI for the detection
        functionality.
    image_managers: List[ImageData]
        List of (relevant) image data management objects providing access to
        loaded image datasets.
    *args : Iterable
        Positional arguments for the ``QWidget`` superclass.
    **kwargs : dict
        Keyword arguments for the ``QWidget`` superclass.


    .. admonition:: Signals

        - :attr:`detected_data`

    .. admonition:: Slots

        - :meth:`images_loaded`
        - :meth:`update_settings`
    """
    used_colors: List[str] = []
    """List[str] : Colors of rods that are supposed to be detected.

    Default is ``[]``.
    """

    number_rods: int = 1
    """int : Expected number of rods per color in one frame.

    Default is ``1``.
    """

    model: torch.ScriptModule = None
    """ScriptModule : Neural network model that is used for detection.

    Default is ``None``.
    """

    detected_data = QtCore.pyqtSignal(pd.DataFrame)
    """pyqtSignal(DataFrame) : Sends data of detected rods for one frame.

    This signal is emitted once for every image during the detection process.
    The ``DataFrame`` in the payload only contains 2D position data as well as
    the frame, color and particle numbers.

    See also
    --------
    :func:`~RodTracker.backend.detection.Detector.run`,
    :func:`~ParticleDetection.utils.helper_funcs.rod_endpoints`,
    :func:`~ParticleDetection.utils.datasets.add_points`
    """

    _active_detections: int = 0
    _started_detections: int = 0
    _progress: float = 1.
    start_frame: int = 0
    """int : First frame for detecting particles in it.

    Default is ``0``.
    """

    end_frame: int = 0
    """int : Last frame for detecting particles in it.

    Default is ``0``.
    """

    _logger: lg.ActionLogger = None
    threshold: float = 0.5
    """float: Confidence threshold :math:`\\in [0, 1]` below which objects are
    rejected after detection.

    Default is ``0.5``.
    """

    def __init__(self, ui: QtWidgets.QWidget, image_managers: List[ImageData],
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = ui
        self._threads = QtCore.QThreadPool()

        self.managers = image_managers
        for manager in self.managers:
            manager.data_loaded.connect(self.images_loaded)
        self.tb_model = ui.findChild(QtWidgets.QToolButton, "tb_model")
        self.le_model = ui.findChild(QtWidgets.QLineEdit, "le_model")
        self.tb_model.clicked.connect(self.load_model)
        self.le_threshold = ui.findChild(QtWidgets.QLineEdit, "le_threshold")
        self.le_threshold.setText(str(self.threshold))
        self.le_threshold.textChanged.connect(self._set_threshold)
        lbl_threshold = ui.findChild(QtWidgets.QLabel, "lbl_threshold")
        lbl_threshold.setText("Confidence Threshold [0.0, 1.0]: ")
        threshold_validator = QtGui.QDoubleValidator(0.0, 1.0, 2)
        self.le_threshold.setValidator(threshold_validator)

        color_group = ui.findChildren(QtWidgets.QGroupBox)[0]
        group_layout: QtWidgets.QGridLayout = color_group.layout()
        for cb in color_group.findChildren(QtWidgets.QCheckBox):
            group_layout.removeWidget(cb)
            cb.hide()
            cb.deleteLater()
        row = 0
        col = 0
        for color in ds.DEFAULT_CLASSES.values():
            cb = QtWidgets.QCheckBox(text=color.lower())
            cb.setObjectName(f"cb_{color}")
            cb.stateChanged.connect(self._toggle_color)
            cb.setChecked(True)
            group_layout.addWidget(cb, row, col)
            if col == 1:
                col = 0
                row += 1
            else:
                col = 1

        self.pb_detect = ui.findChild(QtWidgets.QPushButton, "pb_detect")
        self.pb_detect.clicked.connect(self.start_detection)

        self.progress = ui.findChild(QtWidgets.QProgressBar,
                                     "progress_detection")
        self.progress.setValue(100)

        self.spb_start_f = ui.findChild(QtWidgets.QSpinBox,
                                        "start_frame_detection")
        self.spb_start_f.valueChanged.connect(self._change_start_frame)
        self.spb_end_f = ui.findChild(QtWidgets.QSpinBox,
                                      "end_frame_detection")
        self.spb_end_f.valueChanged.connect(self._change_end_frame)

    def _set_threshold(self, val: str):
        try:
            new_threshold = float(val)
            if new_threshold < 0.0:
                new_threshold = 0.0
                self.le_threshold.setText(str(new_threshold))
            elif new_threshold > 1.00:
                new_threshold = 1.0
                self.le_threshold.setText(str(new_threshold))
            self.threshold = new_threshold
            _logger.info(self.threshold)
        except ValueError:
            self.threshold = 0.0
            self.le_threshold.setText(str(self.threshold))

    def _change_start_frame(self, new_val: int):
        """Callback for the ``QSpinBox`` handling the start frame selection."""
        self.start_frame = new_val

    def _change_end_frame(self, new_val: int):
        """Callback for the ``QSpinBox`` handling the end frame selection."""
        self.end_frame = new_val

    def _toggle_color(self, _: int):
        """Update whether to use an available color.

        Parameters
        ----------
        _ : int
        """
        self.used_colors = []
        for cb in self.ui.findChildren(QtWidgets.QCheckBox):
            if "tracking" in cb.objectName():
                continue
            if cb.checkState():
                self.used_colors.append(cb.objectName().split("_")[1])

    def load_model(self):
        """Show a file selection dialog to a user to select a particle
        detection model.

        Lets the user select a ``*.pt`` file that should contain their desired
        particle detection model. The file is then loaded and the contained
        model set for use in the next detection(s).

        Returns
        -------
        None

        See also
        --------
        :mod:`ParticleDetection.modelling.export`
        """
        ui_dir = self.le_model.text()
        # opens directory to select image
        kwargs = {}
        # handle file path issue when running on linux as a snap
        if 'SNAP' in os.environ:
            kwargs["options"] = QtWidgets.QFileDialog.DontUseNativeDialog
        chosen_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.le_model, 'Open a detection model', ui_dir, '*.pt',
            **kwargs)
        if chosen_file == "":
            # File selection was aborted
            return None
        else:
            self.le_model.setText(chosen_file)
            self.model = torch.jit.load(chosen_file)
            self.pb_detect.setEnabled(True)

    def autoselect_range(self):
        """**Not Implemented.**"""
        raise NotImplementedError

    @QtCore.pyqtSlot(int, str, object)
    def images_loaded(self, num_imgs: int, id: str, path):
        """Hook to update the available frame range for detection.

        This function is intended as a slot for the
        :attr:`~.ImageData.data_loaded` signal which in this case acts as an
        indicator for new image data availability. The available range of
        frames is updated with the information stored in the object, that
        emitted the signal.

        Parameters
        ----------
        num_imgs : int
            Variable to match the :attr:`~.ImageData.data_loaded` signal
            signature. Otherwise not used.
        id : str
            ID of the image management object, that has updated its loaded
            dataset. This object is then used for updating the available frames
            for detection of particles.
        path : Any
            Variable to match the :attr:`~.ImageData.data_loaded` signal
            signature. Otherwise not used.

        Returns
        -------
        None
        """
        for img_manager in self.managers:
            if img_manager.data_id != id:
                continue
            min_f = min(img_manager.frames)
            max_f = max(img_manager.frames)
            self.spb_start_f.setRange(min_f, max_f)
            self.spb_end_f.setRange(min_f, max_f)
            self.spb_start_f.setValue(min_f)
            self.spb_end_f.setValue(max_f)

    def start_detection(self):
        """(Re-)Start the detection process.

        Starts a detection process for each dataset loaded in the
        :attr:`managers` attribute. All frames between :attr:`start_frame` and
        :attr:`end_frame` are used and only the selected colors in
        :attr:`used_colors` will be detected.
        This function cannot start the detection without a loaded
        :attr:`model`.

        Returns
        -------
        None
        """
        if self.model is None:
            _logger.info("No model selected yet.")
            return
        self.progress.setValue(0)
        self._progress = 0.

        for img_manager in self.managers:
            if not img_manager.data_id:
                continue
            self._active_detections += 1
            self._started_detections += 1
            idx_start = img_manager.frames.index(self.start_frame)
            idx_end = img_manager.frames.index(self.end_frame)
            detector = Detector(img_manager.data_id, self.model,
                                img_manager.files[idx_start:idx_end + 1],
                                img_manager.frames[idx_start:idx_end + 1],
                                self.used_colors, self.threshold)
            detector.signals.progress.connect(self._progress_update)
            detector.signals.finished.connect(self._detection_finished)
            detector.signals.error.connect(
                lambda ret: lg.exception_logger(*ret))
            self._threads.start(detector)
        self.pb_detect.setEnabled(False)

    @QtCore.pyqtSlot(str)
    def _detection_finished(self, cam_id: str):
        """Hook to clean up after each detection process finished.

        Updates the active detections and resets the UI for more detections
        after all detection processes/threads have finished.

        Parameters
        ----------
        cam_id : str
            ID of the :class:`ImageData` object for which the detection process
            was started.
            Is not used.

        Returns
        -------
        None
        """
        self._active_detections -= 1
        if self._active_detections == 0:
            self.pb_detect.setEnabled(True)
            self._started_detections = 0
            self._progress = 1.0
            self.progress.setValue(100)

    @QtCore.pyqtSlot(float, pd.DataFrame, str)
    def _progress_update(self, val: float, data: pd.DataFrame, cam_id: str):
        """Accepts progress reports of a detection process, logs and propagates
        them.

        Parameters
        ----------
        val : float
            Progression value of the detection process/thread
            :math:`\\in [0, 1]`.
        data : pd.DataFrame
            The ``DataFrame`` containing the detected 2D particle position data
            as well as the frame, color and particle numbers.
        cam_id : str
            ID of the :class:`ImageData` object for which the detection process
            was started.


        .. hint::

            **Emits**

                - :attr:`detected_data`
        """
        self._progress += (val / self._started_detections)
        self.progress.setValue(int(100 * self._progress))
        if self._logger is not None:
            frame = data["frame"].unique()[0]
            action = RodDetection(frame, cam_id, len(data))
            self._logger.add_action(action)
        self.detected_data.emit(data)

    @QtCore.pyqtSlot(dict)
    def update_settings(self, settings: dict) -> None:
        """Catches updates of the settings from a `Settings` class.

        Checks for the keys relevant to itself and updates the corresponding
        attributes. Redraws itself with the new settings in place.

        Parameters
        ----------
        settings : dict

        Returns
        -------
        None
        """
        if "number_rods" in settings:
            self.number_rods = settings["number_rods"]
