import json
from abc import abstractmethod

from PyQt5 import QtWidgets, QtCore
from Python.ui.dialogs import SettingsDialog
from Python.backend.logger import TEMP_DIR


class Configuration(QtCore.QObject):
    """Generic class that shall hold configurations/settings."""
    __default: dict
    _contents: dict
    path: str = TEMP_DIR + "/configurations.json"

    def read(self, path: str = None):
        """Reads configurations from a file and saves them in this object.

        Parameters
        ----------
        path : str, optional
            Path of the file to read. If no path is given the classes saved
            path is used, this might be the default path or a programmatically
            exchanged path

        Returns
        -------
        None
        """
        if path is None:
            path = self.path
        with open(path, 'r') as f:
            contents = json.load(f)
            if contents is None:
                raise FileNotFoundError
            else:
                self._contents = contents

    @abstractmethod
    def reset_to_default(self):
        """Resets the configuration values to their defaults."""
        pass

    @abstractmethod
    def show_dialog(self, parent):
        """Displays a dialog for the user to change the configuration(s)."""
        pass

    @classmethod
    def save(cls, new_path: str = None, new_data: dict = None):
        """Saves the `contents` to a location on disk.

        The saving location is determined by the objects property `path` if
        the parameter is left out.

        Parameters
        ----------
        new_path : str, optional
            Location to save the contents to. If this parameter is left
            blank the Configuration objects path property is used.
        new_data : dict, optional
            Configuration data, that is supposed to be saved and therefore
            replace the old configuration data.

        Returns
        -------
        None
        """
        if new_data is not None:
            cls._contents = new_data
        if new_path is not None:
            cls.path = new_path
        to_file = json.dumps(cls._contents, indent=2)
        with open(cls.path, 'w') as out:
            out.write(to_file)


class Settings(Configuration):
    """Holds settings for the GUI.

    Parameters
    ----------
    path : str, optional
        Location and name where the settings are saved as a *.json file. The
        default location is used, if no path is given.

    Attributes
    ----------
    path : str
        Location and name where the settings are saved as a *.json file.
    parent : QWidget

    Signals
    -------
    settings_changed(dict)
    """
    path = TEMP_DIR + "/settings.json"
    __default = {
        "visual": {
            "rod_thickness": 3,
            "rod_color": [0, 255, 255],
            "number_offset": 15,
            "number_color": [0, 0, 0],
            "number_size": 11,
            "boundary_offset": 5
        },
        "data": {
            "images_root": "./",
            "positions_root": "./",
        }
    }
    _contents = __default
    parent: QtWidgets.QMainWindow
    settings_changed = QtCore.pyqtSignal([dict], name="settings_changed")

    def __init__(self, path: str = None):
        super().__init__()
        if path is not None:
            self.path = path
        self.read()

    def read(self, path: str = None):
        try:
            super().read(path)
        except FileNotFoundError:
            if path is None:
                path = self.path
            if self._contents is None:
                self.reset_to_default()
            self.save(new_path=path)
        self.send_settings()

    def reset_to_default(self):
        self._contents = self.__default
        self.send_settings()

    def send_settings(self):
        """Notifies subscribers of `settings_changed` about settings changes.

        Emits a `settings_changed` signal for every category of settings.
        """
        self.settings_changed.emit(self._contents["visual"])
        self.settings_changed.emit(self._contents["data"])

    def show_dialog(self, parent: QtWidgets.QMainWindow):
        self.parent = parent
        settings_dialog = SettingsDialog(self._contents, parent,
                                         self.__default)
        if settings_dialog.exec():
            self.parent.statusBar().showMessage("Saved settings changes. "
                                                "Right click to see rod "
                                                "numbers.",
                                                4000)
            self._contents = settings_dialog.tmp_contents
            self.save(new_data=self._contents)
            self.send_settings()
        else:
            self.parent.statusBar().showMessage("Discarded settings "
                                                "changes.", 4000)
            return
