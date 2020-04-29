# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 530, 343, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(410, 20, 201, 20))
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.synopsisLabel = QtWidgets.QLabel(self.centralwidget)
        self.synopsisLabel.setGeometry(QtCore.QRect(120, 650, 801, 91))
        self.synopsisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.synopsisLabel.setObjectName("synopsisLabel")
        self.contentLabel = QtWidgets.QLabel(self.centralwidget)
        self.contentLabel.setGeometry(QtCore.QRect(290, 90, 441, 351))
        self.contentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.contentLabel.setObjectName("contentLabel")
        self.synopsisLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.synopsisLabel2.setGeometry(QtCore.QRect(120, 770, 801, 91))
        self.synopsisLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.synopsisLabel2.setObjectName("synopsisLabel2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.titleLabel.setText(_translate("MainWindow", "Video Image and Synopsis Tool"))
        self.synopsisLabel.setText(_translate("MainWindow", "Synopsis"))
        self.contentLabel.setText(_translate("MainWindow", "Content"))
        self.synopsisLabel2.setText(_translate("MainWindow", "Synopsis2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
