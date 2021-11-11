# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'track_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 532)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon_main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralized = QtWidgets.QWidget(MainWindow)
        self.centralized.setObjectName("centralized")
        self.gridLayout = QtWidgets.QGridLayout(self.centralized)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralized)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_all = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_all.setGeometry(QtCore.QRect(0, 0, 1054, 473))
        self.scrollAreaWidgetContents_all.setObjectName("scrollAreaWidgetContents_all")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_all)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hl_controlbar = QtWidgets.QHBoxLayout()
        self.hl_controlbar.setObjectName("hl_controlbar")
        self.grid_loads = QtWidgets.QGridLayout()
        self.grid_loads.setObjectName("grid_loads")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_all)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.grid_loads.addWidget(self.line_2, 1, 0, 1, 2)
        self.pb_load_images = QtWidgets.QPushButton(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_load_images.sizePolicy().hasHeightForWidth())
        self.pb_load_images.setSizePolicy(sizePolicy)
        self.pb_load_images.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pb_load_images.setObjectName("pb_load_images")
        self.grid_loads.addWidget(self.pb_load_images, 0, 0, 1, 1)
        self.pb_load_rods = QtWidgets.QPushButton(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_load_rods.sizePolicy().hasHeightForWidth())
        self.pb_load_rods.setSizePolicy(sizePolicy)
        self.pb_load_rods.setObjectName("pb_load_rods")
        self.grid_loads.addWidget(self.pb_load_rods, 2, 0, 1, 1)
        self.le_image_dir = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_image_dir.sizePolicy().hasHeightForWidth())
        self.le_image_dir.setSizePolicy(sizePolicy)
        self.le_image_dir.setMinimumSize(QtCore.QSize(100, 0))
        self.le_image_dir.setMaximumSize(QtCore.QSize(400, 16777215))
        self.le_image_dir.setObjectName("le_image_dir")
        self.grid_loads.addWidget(self.le_image_dir, 0, 1, 1, 1)
        self.le_rod_dir = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_rod_dir.sizePolicy().hasHeightForWidth())
        self.le_rod_dir.setSizePolicy(sizePolicy)
        self.le_rod_dir.setMinimumSize(QtCore.QSize(100, 0))
        self.le_rod_dir.setMaximumSize(QtCore.QSize(400, 16777215))
        self.le_rod_dir.setObjectName("le_rod_dir")
        self.grid_loads.addWidget(self.le_rod_dir, 2, 1, 1, 1)
        self.hl_controlbar.addLayout(self.grid_loads)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_all)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.hl_controlbar.addWidget(self.line_3)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem1)
        self.group_rod_color = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_rod_color.sizePolicy().hasHeightForWidth())
        self.group_rod_color.setSizePolicy(sizePolicy)
        self.group_rod_color.setObjectName("group_rod_color")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.group_rod_color)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rb_red = QtWidgets.QRadioButton(self.group_rod_color)
        self.rb_red.setObjectName("rb_red")
        self.gridLayout_4.addWidget(self.rb_red, 0, 3, 1, 1)
        self.rb_purple = QtWidgets.QRadioButton(self.group_rod_color)
        self.rb_purple.setObjectName("rb_purple")
        self.gridLayout_4.addWidget(self.rb_purple, 0, 2, 1, 1)
        self.rb_black = QtWidgets.QRadioButton(self.group_rod_color)
        self.rb_black.setChecked(True)
        self.rb_black.setObjectName("rb_black")
        self.gridLayout_4.addWidget(self.rb_black, 0, 1, 1, 1)
        self.rb_green = QtWidgets.QRadioButton(self.group_rod_color)
        self.rb_green.setObjectName("rb_green")
        self.gridLayout_4.addWidget(self.rb_green, 1, 1, 1, 1)
        self.rb_blue = QtWidgets.QRadioButton(self.group_rod_color)
        self.rb_blue.setObjectName("rb_blue")
        self.gridLayout_4.addWidget(self.rb_blue, 1, 2, 1, 1)
        self.rb_yellow = QtWidgets.QRadioButton(self.group_rod_color)
        self.rb_yellow.setObjectName("rb_yellow")
        self.gridLayout_4.addWidget(self.rb_yellow, 1, 3, 1, 1)
        self.hl_controlbar.addWidget(self.group_rod_color)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.le_rod_disp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_rod_disp.sizePolicy().hasHeightForWidth())
        self.le_rod_disp.setSizePolicy(sizePolicy)
        self.le_rod_disp.setStyleSheet("background-color: transparent; font-weight: bold;")
        self.le_rod_disp.setFrame(False)
        self.le_rod_disp.setReadOnly(True)
        self.le_rod_disp.setPlaceholderText("")
        self.le_rod_disp.setObjectName("le_rod_disp")
        self.verticalLayout_3.addWidget(self.le_rod_disp)
        self.cb_overlay = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_overlay.sizePolicy().hasHeightForWidth())
        self.cb_overlay.setSizePolicy(sizePolicy)
        self.cb_overlay.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cb_overlay.setChecked(True)
        self.cb_overlay.setObjectName("cb_overlay")
        self.verticalLayout_3.addWidget(self.cb_overlay)
        spacerItem3 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.group_disp_method = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_disp_method.sizePolicy().hasHeightForWidth())
        self.group_disp_method.setSizePolicy(sizePolicy)
        self.group_disp_method.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.group_disp_method.setObjectName("group_disp_method")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.group_disp_method)
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rb_disp_all = QtWidgets.QRadioButton(self.group_disp_method)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_disp_all.sizePolicy().hasHeightForWidth())
        self.rb_disp_all.setSizePolicy(sizePolicy)
        self.rb_disp_all.setChecked(True)
        self.rb_disp_all.setObjectName("rb_disp_all")
        self.verticalLayout_4.addWidget(self.rb_disp_all)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb_disp_one = QtWidgets.QRadioButton(self.group_disp_method)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_disp_one.sizePolicy().hasHeightForWidth())
        self.rb_disp_one.setSizePolicy(sizePolicy)
        self.rb_disp_one.setMinimumSize(QtCore.QSize(70, 0))
        self.rb_disp_one.setObjectName("rb_disp_one")
        self.horizontalLayout_3.addWidget(self.rb_disp_one)
        self.le_disp_one = QtWidgets.QLineEdit(self.group_disp_method)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_disp_one.sizePolicy().hasHeightForWidth())
        self.le_disp_one.setSizePolicy(sizePolicy)
        self.le_disp_one.setMaximumSize(QtCore.QSize(40, 16777215))
        self.le_disp_one.setObjectName("le_disp_one")
        self.horizontalLayout_3.addWidget(self.le_disp_one)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.group_disp_method)
        self.hl_controlbar.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem4)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_all)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.hl_controlbar.addWidget(self.line_4)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_frame_disp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_frame_disp.sizePolicy().hasHeightForWidth())
        self.le_frame_disp.setSizePolicy(sizePolicy)
        self.le_frame_disp.setStyleSheet("background-color: transparent;font-weight: bold;")
        self.le_frame_disp.setFrame(False)
        self.le_frame_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.le_frame_disp.setReadOnly(True)
        self.le_frame_disp.setPlaceholderText("")
        self.le_frame_disp.setObjectName("le_frame_disp")
        self.verticalLayout_2.addWidget(self.le_frame_disp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_previous = QtWidgets.QPushButton(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_previous.sizePolicy().hasHeightForWidth())
        self.pb_previous.setSizePolicy(sizePolicy)
        self.pb_previous.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pb_previous.setObjectName("pb_previous")
        self.horizontalLayout.addWidget(self.pb_previous)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pb_next = QtWidgets.QPushButton(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_next.sizePolicy().hasHeightForWidth())
        self.pb_next.setSizePolicy(sizePolicy)
        self.pb_next.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pb_next.setObjectName("pb_next")
        self.horizontalLayout.addWidget(self.pb_next)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.slider_frames = QtWidgets.QSlider(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_frames.sizePolicy().hasHeightForWidth())
        self.slider_frames.setSizePolicy(sizePolicy)
        self.slider_frames.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frames.setObjectName("slider_frames")
        self.verticalLayout_2.addWidget(self.slider_frames)
        self.hl_controlbar.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem7)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_all)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.hl_controlbar.addWidget(self.line_5)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_controlbar.addItem(spacerItem8)
        self.grid_save = QtWidgets.QGridLayout()
        self.grid_save.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.grid_save.setObjectName("grid_save")
        self.le_save_dir = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_save_dir.sizePolicy().hasHeightForWidth())
        self.le_save_dir.setSizePolicy(sizePolicy)
        self.le_save_dir.setMinimumSize(QtCore.QSize(100, 0))
        self.le_save_dir.setMaximumSize(QtCore.QSize(400, 16777215))
        self.le_save_dir.setObjectName("le_save_dir")
        self.grid_save.addWidget(self.le_save_dir, 0, 1, 1, 1)
        self.pb_save_rods = QtWidgets.QPushButton(self.scrollAreaWidgetContents_all)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_save_rods.sizePolicy().hasHeightForWidth())
        self.pb_save_rods.setSizePolicy(sizePolicy)
        self.pb_save_rods.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pb_save_rods.setObjectName("pb_save_rods")
        self.grid_save.addWidget(self.pb_save_rods, 0, 0, 1, 1)
        self.hl_controlbar.addLayout(self.grid_save)
        self.verticalLayout.addLayout(self.hl_controlbar)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_all)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_19.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.camera_tabs = QtWidgets.QTabWidget(self.splitter)
        self.camera_tabs.setObjectName("camera_tabs")
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.sa_camera_0 = QtWidgets.QScrollArea(self.tab_0)
        self.sa_camera_0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sa_camera_0.setWidgetResizable(True)
        self.sa_camera_0.setObjectName("sa_camera_0")
        self.scrollAreaWidgetContents_0 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_0.setGeometry(QtCore.QRect(0, 0, 502, 274))
        self.scrollAreaWidgetContents_0.setObjectName("scrollAreaWidgetContents_0")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.camera_0 = RodImageWidget(self.scrollAreaWidgetContents_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_0.sizePolicy().hasHeightForWidth())
        self.camera_0.setSizePolicy(sizePolicy)
        self.camera_0.setMouseTracking(True)
        self.camera_0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.camera_0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.camera_0.setText("")
        self.camera_0.setPixmap(QtGui.QPixmap("resources/icon_main.ico"))
        self.camera_0.setScaledContents(False)
        self.camera_0.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_0.setObjectName("camera_0")
        self.verticalLayout_16.addWidget(self.camera_0)
        self.sa_camera_0.setWidget(self.scrollAreaWidgetContents_0)
        self.verticalLayout_15.addWidget(self.sa_camera_0)
        self.camera_tabs.addTab(self.tab_0, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.sa_camera_1 = QtWidgets.QScrollArea(self.tab_1)
        self.sa_camera_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sa_camera_1.setWidgetResizable(True)
        self.sa_camera_1.setObjectName("sa_camera_1")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 274, 274))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.camera_1 = RodImageWidget(self.scrollAreaWidgetContents_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_1.sizePolicy().hasHeightForWidth())
        self.camera_1.setSizePolicy(sizePolicy)
        self.camera_1.setMouseTracking(True)
        self.camera_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.camera_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.camera_1.setText("")
        self.camera_1.setPixmap(QtGui.QPixmap("resources/icon_main.ico"))
        self.camera_1.setScaledContents(False)
        self.camera_1.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_1.setObjectName("camera_1")
        self.verticalLayout_18.addWidget(self.camera_1)
        self.sa_camera_1.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_17.addWidget(self.sa_camera_1)
        self.camera_tabs.addTab(self.tab_1, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.undo_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.undo_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.undo_layout.setContentsMargins(0, 0, 0, 0)
        self.undo_layout.setObjectName("undo_layout")
        self.lv_actions_list = ActionLoggerWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lv_actions_list.sizePolicy().hasHeightForWidth())
        self.lv_actions_list.setSizePolicy(sizePolicy)
        self.lv_actions_list.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lv_actions_list.setObjectName("lv_actions_list")
        self.undo_layout.addWidget(self.lv_actions_list)
        self.pb_undo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_undo.sizePolicy().hasHeightForWidth())
        self.pb_undo.setSizePolicy(sizePolicy)
        self.pb_undo.setMinimumSize(QtCore.QSize(60, 0))
        self.pb_undo.setMaximumSize(QtCore.QSize(400, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/left-arrow-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_undo.setIcon(icon1)
        self.pb_undo.setObjectName("pb_undo")
        self.undo_layout.addWidget(self.pb_undo)
        self.verticalLayout_19.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_all)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralized)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setEnabled(True)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setEnabled(True)
        self.action_save.setObjectName("action_save")
        self.action_zoom_in = QtWidgets.QAction(MainWindow)
        self.action_zoom_in.setObjectName("action_zoom_in")
        self.action_zoom_out = QtWidgets.QAction(MainWindow)
        self.action_zoom_out.setObjectName("action_zoom_out")
        self.action_original_size = QtWidgets.QAction(MainWindow)
        self.action_original_size.setObjectName("action_original_size")
        self.action_fit_to_window = QtWidgets.QAction(MainWindow)
        self.action_fit_to_window.setEnabled(True)
        self.action_fit_to_window.setObjectName("action_fit_to_window")
        self.action_persistent_view = QtWidgets.QAction(MainWindow)
        self.action_persistent_view.setCheckable(True)
        self.action_persistent_view.setChecked(True)
        self.action_persistent_view.setObjectName("action_persistent_view")
        self.action_revert = QtWidgets.QAction(MainWindow)
        self.action_revert.setObjectName("action_revert")
        self.action_redo = QtWidgets.QAction(MainWindow)
        self.action_redo.setEnabled(True)
        self.action_redo.setObjectName("action_redo")
        self.action_cleanup = QtWidgets.QAction(MainWindow)
        self.action_cleanup.setObjectName("action_cleanup")
        self.action_open_rods = QtWidgets.QAction(MainWindow)
        self.action_open_rods.setObjectName("action_open_rods")
        self.action_preferences = QtWidgets.QAction(MainWindow)
        self.action_preferences.setObjectName("action_preferences")
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_open_rods)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_preferences)
        self.menuEdit.addAction(self.action_revert)
        self.menuEdit.addAction(self.action_redo)
        self.menuEdit.addAction(self.action_cleanup)
        self.menuView.addAction(self.action_persistent_view)
        self.menuView.addAction(self.action_zoom_in)
        self.menuView.addAction(self.action_zoom_out)
        self.menuView.addAction(self.action_original_size)
        self.menuView.addAction(self.action_fit_to_window)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.camera_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rod Tracker"))
        self.pb_load_images.setText(_translate("MainWindow", "Load Images"))
        self.pb_load_rods.setText(_translate("MainWindow", "Load Rods"))
        self.group_rod_color.setTitle(_translate("MainWindow", "Rod Color"))
        self.rb_red.setText(_translate("MainWindow", "Red"))
        self.rb_purple.setText(_translate("MainWindow", "Purple"))
        self.rb_black.setText(_translate("MainWindow", "Black"))
        self.rb_green.setText(_translate("MainWindow", "Green"))
        self.rb_blue.setText(_translate("MainWindow", "Blue"))
        self.rb_yellow.setText(_translate("MainWindow", "Yellow"))
        self.le_rod_disp.setText(_translate("MainWindow", "Loaded Rods: 0"))
        self.cb_overlay.setText(_translate("MainWindow", "Overlay Rods"))
        self.group_disp_method.setTitle(_translate("MainWindow", "Display Methods"))
        self.rb_disp_all.setText(_translate("MainWindow", "All Rods"))
        self.rb_disp_one.setText(_translate("MainWindow", "Rod No.:"))
        self.le_frame_disp.setText(_translate("MainWindow", "Frame: ???"))
        self.pb_previous.setToolTip(_translate("MainWindow", "Previous Image"))
        self.pb_previous.setText(_translate("MainWindow", "Previous"))
        self.pb_previous.setShortcut(_translate("MainWindow", "Left"))
        self.pb_next.setToolTip(_translate("MainWindow", "Next Image"))
        self.pb_next.setText(_translate("MainWindow", "Next"))
        self.pb_next.setShortcut(_translate("MainWindow", "Right"))
        self.pb_save_rods.setText(_translate("MainWindow", "Save"))
        self.camera_tabs.setTabText(self.camera_tabs.indexOf(self.tab_0), _translate("MainWindow", "Front View (FV)"))
        self.camera_tabs.setTabText(self.camera_tabs.indexOf(self.tab_1), _translate("MainWindow", "Top View (TV)"))
        self.pb_undo.setText(_translate("MainWindow", "Undo"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.action_open.setText(_translate("MainWindow", "Open Images"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_zoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.action_zoom_in.setShortcut(_translate("MainWindow", "+"))
        self.action_zoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.action_zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.action_original_size.setText(_translate("MainWindow", "Original Size"))
        self.action_original_size.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_fit_to_window.setText(_translate("MainWindow", "Fit to Window"))
        self.action_persistent_view.setText(_translate("MainWindow", "Persistent View"))
        self.action_revert.setText(_translate("MainWindow", "Undo"))
        self.action_revert.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_redo.setText(_translate("MainWindow", "Redo"))
        self.action_redo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.action_cleanup.setText(_translate("MainWindow", "Cleanup Data"))
        self.action_open_rods.setText(_translate("MainWindow", "Open Rod Data"))
        self.action_preferences.setText(_translate("MainWindow", "Preferences"))
from actionlogger import ActionLoggerWidget
from rodimagewidget import RodImageWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
