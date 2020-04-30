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
from PyQt5.QtWidgets import *
import pickle

SYNOPSIS_FRAME_HEIGHT = 72
SYNOPSIS_FRAME_WIDTH = 88
SYNOPSIS_FRAMES_PER_ROW = 10
BASE_DIR = "/Users/Sai/Desktop/VideoSynopsis/"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.widgetStack = QStackedWidget(self.centralwidget)
        self.widgetStack.setGeometry(QtCore.QRect(325, 100, 352, 288))
        self.widgetStack.setObjectName("widgetStack")

        
        self.videoWidget = QtWidgets.QWidget(self.centralwidget)
        self.videoWidget = VideoPlayer()
        self.videoWidget.setGeometry(QtCore.QRect(325, 100, 352, 288))
        self.videoWidget.setObjectName("videoWidget")

        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(325, 100, 352, 288))
        self.imageLabel.setStyleSheet("background-color: black")
        self.imageLabel.setObjectName("imageWidget")



        self.widgetStack.addWidget(self.videoWidget)
        self.widgetStack.addWidget(self.imageLabel)

        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 400, 400, 80))
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
        self.synopsisLabel.setGeometry(QtCore.QRect(60, 500, 880, 144))
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
        
        self.playButton.clicked.connect(self.playMediaButton)
        self.pauseButton.clicked.connect(self.pauseMediaButton)
        self.stopButton.clicked.connect(self.stopMediaButton)

        self.synopsisLabel.mousePressEvent = self.mousePressEvent
        self.setMetaData("/Users/Sai/Desktop/VideoSynopsis/metadata.pkl")

        self.mediaFile =  "/Users/Sai/Desktop/video_1.mp4"
        self.mediaPosition = 0


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
        data = self.metaData[frame_index].split(',')
        if(float(data[3])==-1):
            print("IMAGE")
            self.setImage(data)
        else:
            print("VIDEO")
            self.setAndPlayMediaButton(data)

    def setImageVideo(self, index):
        self.widgetStack.setCurrentIndex(index)

    def setImage(self, data):
        file = data[1]
        mediaFile = BASE_DIR+file
        self.stopMediaButton()
        self.imageLabel.setPixmap(QPixmap(mediaFile))
        self.setImageVideo(1)       # show the image widget

    def playMediaButton(self):
        print("Playing", self.mediaFile)
        self.setImageVideo(0)
        self.videoWidget.mediaPlayer.play()

    def setAndPlayMediaButton(self, data):
        file = data[1]
        mediaFile = BASE_DIR+file
        mediaFile = mediaFile.strip()
        position = int(float(data[2]))* 1000 # need in miliseconds
        if position > 200:
            position -= 200
        print(data)
        self.setImageVideo(0)
        self.mediaPosition = position
        self.videoWidget.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(mediaFile)))
        self.videoWidget.mediaPlayer.setPosition(position)
        self.videoWidget.mediaPlayer.play()
        # self.videoWidget.mediaPlayer.pause()
        

    def pauseMediaButton(self):
        print("Pausing", self.mediaFile)
        self.setImageVideo(0)
        self.videoWidget.mediaPlayer.pause()

    def stopMediaButton(self):
        print("Stopping", self.mediaFile)
        self.setImageVideo(0)
        self.videoWidget.mediaPlayer.stop()
        self.videoWidget.mediaPlayer.setPosition(self.mediaPosition)





class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()


        self.filename = "/Users/Sai/Desktop/video_1.mp4"

        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
 
        #create videowidget object
 
        self.videowidget = QVideoWidget(self)
        self.videowidget.setGeometry(QtCore.QRect(0, 0, 352, 288))

        self.mediaPlayer.setVideoOutput(self.videowidget)
 
        self.show()

 
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
