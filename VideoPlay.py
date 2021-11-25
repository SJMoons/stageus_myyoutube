from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, \
    QVBoxLayout, QAction, QFileDialog, QApplication
import sys
import vlc
import time
import Config
import pafy
import PlayListPage

class VideoPlay:
    def __init__(self,revui,revdb,index,list,num):
        self.number = num
        self.intermediateNum = 0
        self.list = list
        self.ui = revui
        self.db = revdb
        self.num = 0
        self.list2= []
        length = 0
        self.videoList = []
        self.videoList = self.db.read("playlistvideo",["playlist"],[self.list[index].text()])
        print(self.list[index].text())
        # videoself.list2 = self.db.read("playlistvideo",["playlist"],[self.self.list2[index2].text()])
        length = len(self.videoList)
        print(self.videoList)
        # print(len(self.videoList))
        if len(self.videoList) == 0:
            self.window = Config.Alert()
            self.window.message.setText("재생목록에 영상이 없습니다")
            self.window.result.show()
        else:
            while True:
                print(self.list2)
                print(length)
                self.ui.scrollAreaWidgetContents2.setGeometry(0,0,300,60+(self.number*70))
                label = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents2)
                label.setStyleSheet("border:1px solid black; background-color: lightgrey; font:10pt \"맑은 고딕\" ;")
                label.setText(self.videoList[length-1][2])
                # print(self.videoList[length-1][2])
                # label.setAlignment(QtCore.Qt.AlignCenter)
                label.setGeometry(0,0,300,50)
                label.setMaximumHeight(50)
                label.setMinimumHeight(50)

                self.list2.append(label)
                self.ui.verticalLayout2.addWidget(self.list2[self.num])
                length -= 1
                self.num += 1
                self.ui.scrollArea2.setWidget(self.ui.scrollAreaWidgetContents2)
                if length == 0:
                    # self.ui.verticalLayout2.deleteLater()
                    # self.list2.clear()
                    break   
            


            
            self.Instance = vlc.Instance()
            self.mediaplayer = self.Instance.media_player_new()

            ##########video frame
            self.videoframe = QtWidgets.QFrame(
                frameShape=QtWidgets.QFrame.Box, frameShadow=QtWidgets.QFrame.Raised
            ) 

            self.videoframe = QFrame(self.ui.videoPlayPage)

            self.videoframe.setGeometry(QtCore.QRect(200, 180, 1000, 500))

            self.videoframe.setFrameShape(QtWidgets.QFrame.Box)

            self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)

            self.vboxlayout = QVBoxLayout()

            self.vboxlayout.addWidget(self.videoframe)

            url = self.videoList[length-1][1]                                
            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url
            Media = self.Instance.media_new(playurl)
            Media.get_mrl()
            self.mediaplayer.set_media(Media)

            if sys.platform == "win32":  # for Windows
                self.mediaplayer.set_hwnd(int(self.videoframe.winId()))

            self.mediaplayer.play()

            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 9)
        self.init_event()

    def init_event(self):
        self.ui.gobackbutton6.clicked.connect(self.goback_btn)
        self.ui.videoBtnList[0].clicked.connect(self.intermediate_course)
        self.ui.randomrepeatBtnList[0].clicked.connect
        for index in range(0,self.num):
        # index = self.num - 1
        # while index >= 0:
            self.list2[index].mousePressEvent = lambda event, num = index : self.playlist_play(event,num)
            # index -= 1

    def playlist_play(self, event, index):
        url = self.videoList[index][1]
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        Media = self.Instance.media_new(playurl)
        Media.get_mrl()
        self.mediaplayer.set_media(Media)

        if sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(int(self.videoframe.winId()))

        self.mediaplayer.play()

    def intermediate_course(self):
        self.intermediateNum += 1
        if self.intermediateNum %2 == 1:
            self.stop_event()
        if self.intermediateNum %2 == 0:
            self.play_event()

    def stop_event(self):
        self.mediaplayer.stop()

    def play_event(self):
        self.mediaplayer.play()



    def goback_btn(self):
        for index in range(0, len(self.list2)):
            self.list2[index].deleteLater()
        self.list2.clear()

        # self.ui.verticalLayout2.deleteLater()
        # self.list2.clear()
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 7)



# # importing pafy module

  
# url of the video
