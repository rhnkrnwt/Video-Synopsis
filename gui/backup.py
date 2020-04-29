# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui7.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, 
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
import pickle

SYNOPSIS_FRAME_HEIGHT = 72
SYNOPSIS_FRAME_WIDTH = 88
SYNOPSIS_FRAMES_PER_ROW = 10

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.videoLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.videoLayoutWidget.setGeometry(QtCore.QRect(300, 100, 400, 400))
        self.videoLayoutWidget.setObjectName("videoLayoutWidget")
        self.videoLayout = QtWidgets.QHBoxLayout(self.videoLayoutWidget)
        self.videoLayout.setContentsMargins(0, 0, 0, 0)
        self.videoLayout.setObjectName("videoLayout")
        
        self.videoWidget = QtWidgets.QWidget(self.centralwidget)
        self.videoWidget = VideoPlayer()
        self.videoWidget.setObjectName("videoWidget")
        self.videoLayout.addWidget(self.videoWidget)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 500, 400, 80))
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
        self.titleLabel.setGeometry(QtCore.QRect(410, 50, 201, 20))
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.synopsisLabel = QtWidgets.QLabel(self.centralwidget)
        self.synopsisLabel.setGeometry(QtCore.QRect(60, 600, 880, 144))
        self.synopsisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.synopsisLabel.setObjectName("synopsisLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.horizontalLayout.addWidget(self.videoWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setSynopsisBackground()
        
        self.playButton.clicked.connect(self.clicked)
        self.pauseButton.clicked.connect(self.clicked)
        self.stopButton.clicked.connect(self.clicked)

        self.synopsisLabel.mousePressEvent = self.mousePressEvent
        self.setMetaData("/Users/Sai/Desktop/VideoSynopsis/metadata.pkl")


    def setMetaData(self, metadata_file):
        with open(metadata_file, "rb") as metadata:
            self.metaData = pickle.load(metadata)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.titleLabel.setText(_translate("MainWindow", "Video Image and Synopsis Tool"))
        self.synopsisLabel.setText(_translate("MainWindow", "Synopsis"))


    def setSynopsisBackground(self):
        self.synopsisLabel.setStyleSheet('QLabel {background-color: black}')
        self.synopsisLabel.setPixmap(QPixmap("/Users/Sai/Desktop/VideoSynopsis/synopsis.png"))

    def clicked(self):
        print("Clicked")
        self.videoWidget.play_video("/Users/Sai/Desktop/VideoSynopsis/CSCI576ProjectMedia/video_1.avi")

    def mousePressEvent(self, event):
        print("Mouse pressed")
        pos = event.pos()
        x = pos.x()
        y = pos.y()

        col = x//SYNOPSIS_FRAME_WIDTH
        row = y//SYNOPSIS_FRAME_HEIGHT
        
        frame_index = SYNOPSIS_FRAMES_PER_ROW*row+col
        print(pos.x(), pos.y())
        print(frame_index)
        print(self.metaData[frame_index])

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
 
 
        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
 
        self.filename = "/Users/Sai/Desktop/VideoSynopsis/CSCI576ProjectMedia/video_1.avi"
        self.init_ui()

 
        self.show()
 
 
    def init_ui(self):
 
        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
 
        #create videowidget object
 
        videowidget = QVideoWidget()

        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
 
 

 
        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)
 
 
 
        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
 
 
        self.setLayout(vboxLayout)
 
        self.mediaPlayer.setVideoOutput(videowidget)


        self.mediaPlayer.stateChanged.connect(self.stateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

    def stateChanged(self, event):
        print("state changed")
        print(self.mediaPlayer.position())
        return True
 
    def positionChanged(self, event):
        print("Position changed")
        print(self.mediaPlayer.position())
        return True

    def durationChanged(self, event):
        print("Duration changed")
        print(self.mediaPlayer.position())
        return True

 
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
 
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
 
 
    def play_video(self, video):
        file = QUrl.fromLocalFile(video)
        self.mediaPlayer.setMedia(QMediaContent(file))
        self.mediaPlayer.play()

 
 
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
 
 
    def handle_errors(self):
        self.playBtn.setEnabled(False)
 
 
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
