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
        MainWindow.resize(800, 600)
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
        self.scrollArea_2 = QtWidgets.QWidget()
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 772, 531))
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollArea_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollArea_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushprevious = QtWidgets.QPushButton(self.scrollArea_2)
        self.pushprevious.setObjectName("pushprevious")
        self.horizontalLayout.addWidget(self.pushprevious)
        self.overlay = QtWidgets.QPushButton(self.scrollArea_2)
        self.overlay.setObjectName("overlay")
        self.horizontalLayout.addWidget(self.overlay)
        self.RodNumber = QtWidgets.QPushButton(self.scrollArea_2)
        self.RodNumber.setEnabled(False)
        self.RodNumber.setObjectName("RodNumber")
        self.horizontalLayout.addWidget(self.RodNumber)
        self.ClearSave = QtWidgets.QPushButton(self.scrollArea_2)
        self.ClearSave.setEnabled(False)
        self.ClearSave.setObjectName("ClearSave")
        self.horizontalLayout.addWidget(self.ClearSave)
        self.pushnext = QtWidgets.QPushButton(self.scrollArea_2)
        self.pushnext.setObjectName("pushnext")
        self.horizontalLayout.addWidget(self.pushnext)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollArea_2)
        self.scrollArea_3.setAutoFillBackground(True)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 475))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Photo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Photo.sizePolicy().hasHeightForWidth())
        self.Photo.setSizePolicy(sizePolicy)
        self.Photo.setMouseTracking(True)
        self.Photo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Photo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Photo.setScaledContents(False)
        self.Photo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Photo.setObjectName("Photo")
        self.gridLayout_2.addWidget(self.Photo, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_3)
        self.scrollArea.setWidget(self.scrollArea_2)
        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralized)
        self.splitter.setFrameShape(QtWidgets.QFrame.Box)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralized)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setEnabled(False)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setEnabled(False)
        self.actionsave.setObjectName("actionsave")
        self.actionzoom_in = QtWidgets.QAction(MainWindow)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.actionzoom_out = QtWidgets.QAction(MainWindow)
        self.actionzoom_out.setObjectName("actionzoom_out")
        self.normalSizeAct = QtWidgets.QAction(MainWindow)
        self.normalSizeAct.setObjectName("normalSizeAct")
        self.fitToWindowAct = QtWidgets.QAction(MainWindow)
        self.fitToWindowAct.setEnabled(False)
        self.fitToWindowAct.setObjectName("fitToWindowAct")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionsave)
        self.menuView.addAction(self.actionzoom_in)
        self.menuView.addAction(self.actionzoom_out)
        self.menuView.addAction(self.normalSizeAct)
        self.menuView.addAction(self.fitToWindowAct)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rod Tracking"))
        self.label.setText(_translate("MainWindow", "Last Action"))
        self.pushprevious.setToolTip(_translate("MainWindow", "Previous Image"))
        self.pushprevious.setText(_translate("MainWindow", "Previous"))
        self.pushprevious.setShortcut(_translate("MainWindow", "Left"))
        self.overlay.setText(_translate("MainWindow", "Overlay"))
        self.RodNumber.setText(_translate("MainWindow", "Rod Number"))
        self.ClearSave.setText(_translate("MainWindow", "Clear/Save"))
        self.pushnext.setToolTip(_translate("MainWindow", "Next Image"))
        self.pushnext.setText(_translate("MainWindow", "Next"))
        self.pushnext.setShortcut(_translate("MainWindow", "Right"))
        self.Photo.setText(_translate("MainWindow", "Please open an image file"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionopen.setText(_translate("MainWindow", "Open"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionsave.setText(_translate("MainWindow", "Save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionzoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionzoom_in.setShortcut(_translate("MainWindow", "+"))
        self.actionzoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionzoom_out.setShortcut(_translate("MainWindow", "-"))
        self.normalSizeAct.setText(_translate("MainWindow", "Original Size"))
        self.normalSizeAct.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.fitToWindowAct.setText(_translate("MainWindow", "Fit to Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
