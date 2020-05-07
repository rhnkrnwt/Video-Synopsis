# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui7.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtWidgets import *
import pickle


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
TITLE_WIDTH = 200
TITLE_HEIGHT = 20
DESCRIPTION_WIDTH = 300
DESCRIPTION_HEIGHT = 288
DISPLAY_WIDTH = 352
DISPLAY_HEIGHT = 288
HORIZONTAL_WIDTH = 400
HORIZONTAL_HEIGHT = 80
SYNOPSIS_FRAME_HEIGHT = 72
SYNOPSIS_FRAME_WIDTH = 88
SYNOPSIS_FRAMES_PER_ROW = 10
SYNOPSIS_ROWS = 2
SYNOPSIS_WIDTH = SYNOPSIS_FRAME_WIDTH * SYNOPSIS_FRAMES_PER_ROW
SYNOPSIS_HEIGHT = SYNOPSIS_FRAME_HEIGHT * SYNOPSIS_ROWS
BASE_DIR = "/Users/Sai/Desktop/VideoSynopsis/"
VAR = "VALUE"
SYNOPSIS_IMAGE = sys.argv[1]
META_DATA = sys.argv[2]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Video Synopsis Tool")
        MainWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        titleLabelX = (WINDOW_WIDTH-TITLE_WIDTH)/2
        titleLabelY = 50
        self.titleLabel.setGeometry(QtCore.QRect(titleLabelX, titleLabelY, TITLE_WIDTH, TITLE_HEIGHT))
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")



        self.widgetStack = QStackedWidget(self.centralwidget)
        widgetX = (WINDOW_WIDTH-DISPLAY_WIDTH)/2
        widgetY = WINDOW_HEIGHT * 0.3
        self.widgetStack.setGeometry(QtCore.QRect(widgetX, widgetY, DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.widgetStack.setObjectName("widgetStack")

        
        self.videoWidget = QtWidgets.QWidget(self.centralwidget)
        self.videoWidget = VideoPlayer()
        videoWidgetX = (WINDOW_WIDTH-DISPLAY_WIDTH)/2
        videoWidgetY = WINDOW_HEIGHT * 0.3        
        self.videoWidget.setGeometry(QtCore.QRect(videoWidgetX, videoWidgetY, DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.videoWidget.setObjectName("videoWidget")

        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        imageLabelX = (WINDOW_WIDTH-DISPLAY_WIDTH)/2
        imageLabelY = WINDOW_HEIGHT * 0.3  
        self.imageLabel.setGeometry(QtCore.QRect(imageLabelX, imageLabelY, DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.imageLabel.setStyleSheet("background-color: black")
        self.imageLabel.setObjectName("imageWidget")

        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        descriptionLabelX = (WINDOW_WIDTH-DESCRIPTION_WIDTH)/2
        descriptionLabelY = WINDOW_HEIGHT * 0.15
        self.descriptionLabel.setGeometry(QtCore.QRect(descriptionLabelX, descriptionLabelY, DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT))
        self.descriptionLabel.setObjectName("descriptionWidget")
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignTop)

        self.widgetStack.addWidget(self.videoWidget)
        self.widgetStack.addWidget(self.imageLabel)

        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        horizontalWidgetX = (WINDOW_WIDTH-DISPLAY_WIDTH)/2 - 20
        horizontalWidgetY = WINDOW_HEIGHT * 0.65
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(horizontalWidgetX, horizontalWidgetY, HORIZONTAL_WIDTH, HORIZONTAL_HEIGHT))
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



        self.synopsisLabel = QtWidgets.QLabel(self.centralwidget)
        synopsisLabelX = (WINDOW_WIDTH-SYNOPSIS_WIDTH)/2
        synopsisLabelY = WINDOW_HEIGHT * 0.75
        self.synopsisLabel.setGeometry(QtCore.QRect(synopsisLabelX, synopsisLabelY, SYNOPSIS_WIDTH, SYNOPSIS_HEIGHT))
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
        self.setMetaData(META_DATA)

        self.mediaFile =  "/Users/Sai/Desktop/VideoSynopsis/data/video_1_m.mp4"
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
        self.synopsisLabel.setPixmap(QPixmap(SYNOPSIS_IMAGE))

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

        descData = {
            "ctype" : "Image",
            "file" : file,
        }
        self.setDescription(descData)


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
        
        descData = {
            "ctype" : "Video",
            "file" : file,
            "pos" : position
        }
        self.setDescription(descData)


        self.setImageVideo(0)
        self.mediaPosition = position
        self.videoWidget.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(mediaFile)))
        self.videoWidget.mediaPlayer.setPosition(position)
        self.videoWidget.mediaPlayer.play()
        # self.videoWidget.mediaPlayer.pause()
        

    def pauseMediaButton(self):
        self.setImageVideo(0)
        self.videoWidget.mediaPlayer.pause()

    def stopMediaButton(self):
        print("Stopping", self.mediaFile)
        self.setImageVideo(0)
        self.videoWidget.mediaPlayer.stop()
        self.videoWidget.mediaPlayer.setPosition(self.mediaPosition)

    def setDescription(self, data):
        desc = ""
        desc += "Content Description \n"
        if "ctype" in data:
            desc += "Content Type: "+str(data["ctype"])+"\n"
        if "file" in data:
            desc += "File: "+str(data["file"])+"\n"
        if "pos" in data:
            seconds = data["pos"]/1000
            desc += "Position: "+str(seconds)+" seconds \n"
        self.descriptionLabel.setText(desc)





class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()


        self.filename = "/Users/Sai/Desktop/VideoSynopsis/data/video_1.mp4"

        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
 
        #create videowidget object
 
        self.videowidget = QVideoWidget(self)
        self.videowidget.setGeometry(QtCore.QRect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT))

        self.mediaPlayer.setVideoOutput(self.videowidget)
 
        self.show()

 
 

print("ARGS")
print(sys.argv)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
