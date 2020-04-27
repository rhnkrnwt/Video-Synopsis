# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Multimedia Synopsis Tool")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(590, 470, 341, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.pauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.playButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(410, 0, 190, 78))
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.playerWidget = QtWidgets.QWidget(self.centralwidget)
        self.playerWidget.setGeometry(QtCore.QRect(570, 110, 371, 301))
        self.playerWidget.setObjectName("playerWidget")
        self.synopsisWidget = QtWidgets.QWidget(self.centralwidget)
        self.synopsisWidget.setGeometry(QtCore.QRect(60, 109, 471, 441))
        self.synopsisWidget.setObjectName("synopsisWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 80, 151, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 80, 181, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.playerWidget.setStyleSheet('background-color: black')
        self.synopsisWidget.setStyleSheet('background-color: black')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.mainLabel.setText(_translate("MainWindow", "Video and Image Synopsis Tool"))
        self.label.setText(_translate("MainWindow", "Synopsis Image"))
        self.label_2.setText(_translate("MainWindow", "Video/Image Display"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
