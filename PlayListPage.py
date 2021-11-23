from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config
import sip
# import sqlite3


class PlayListPage:
    def __init__(self,revui,revdb):
        self.list = []
        self.list2 = []
        self.ui = revui
        self.db = revdb
        getPlayList = self.db.read("playlist",["playlist"],[""])
        if len(getPlayList) == 0:
            self.all = self.db.cur.execute("SELECT * FROM playlist;")
            self.allPlayList = self.all.fetchall()
            self.listLenth = len(self.allPlayList)
            self.num = 0
            self.exist_playlist()
        self._init__event()

    def _init__event(self):
        self.ui.makePlayList.clicked.connect(self.make_playlist)

    def make_playlist(self):
        self.window = Config.Warning()
        self.inputLabel = QtWidgets.QLineEdit(self.window.result)
        self.inputLabel.setGeometry(83,15,140,30)
        self.inputLabel.setStyleSheet("border:1px solid black;")
        self.window.result.show()
        self.window.confirm.clicked.connect(self.produce_playlist)

    def produce_playlist(self):
        playlistName = self.inputLabel.text()
        recvPlaylist = self.db.read("playlist",["playlist"],[playlistName])
        if len(playlistName) == 0:
            self.window = Config.Alert()
            self.window.message.setText("재생목록의 제목을 입력해주세요.")
            self.window.result.show()

        elif len(recvPlaylist) == 1:
            self.window = Config.Alert()
            self.window.message.setText("이미 있는 플레이리스트 입니다.")
            self.window.result.show()
        
        else:
            self.db.create("playlist",["playlist"],[playlistName])
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+(self.num*60))
            self.label = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
            self.label.setStyleSheet("border:1px solid black; background-color: lightgrey; font:18pt \"맑은 고딕\" ;")
            self.label.setText(playlistName)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setGeometry(0,0,500,50)
            self.label.setMaximumHeight(50)
            self.label.setMinimumHeight(50)

            self.trashBtnList2 = []
            for index in range(0,2):
                playtrashBtn = QtWidgets.QPushButton(self.label)
                xPos = 900 + (index*50)
                if index == 0:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/playbutton.jpg); border: '';")
                    # self.trashBtnList.append(playtrashBtn)
                if index == 1:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/trashcanbutton.png); border: '';")
                    self.trashBtnList2.append(playtrashBtn)

            self.list2.append(self.label)
            self.ui.verticalLayout.addWidget(self.list[self.num])
            self.num += 1
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
            print(self.trashBtnList2)
            self.trashBtnList2[0].clicked.connect(self.delete_playlist)

    def delete_playlist(self):
        for index in range(0,self.listLenth):
            self.trashBtnList[index].mousePressEvent = lambda event, num = index : self.delete_event(event, num)
        for index in range(0,self.num):
            self.trashBtnList2[index].mousePressEvent = lambda event, num = index : self.delete_event2(event, num)

    def delete_event(self, event, index):
        self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+((index-1)*60))
        self.ui.list[1].setparent(None)
    def exist_playlist(self):
        while True:
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+(self.num*60))
            self.label = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
            self.label.setStyleSheet("border:1px solid black; background-color: lightgrey; font:18pt \"맑은 고딕\" ;")
            self.label.setText(self.allPlayList[self.num][0])
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setGeometry(0,0,500,50)
            self.label.setMaximumHeight(50)
            self.label.setMinimumHeight(50)

            self.trashBtnList = []
            for index in range(0,2):
                playtrashBtn = QtWidgets.QPushButton(self.label)
                xPos = 900 + (index*50)
                if index == 0:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/playbutton.jpg); border: '';")
                    # self.playtrashBtnList.append(playtrashBtn)
                if index == 1:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/trashcanbutton.png); border: '';")
                    self.trashBtnList.append(playtrashBtn)

            self.list.append(self.label)
            self.ui.verticalLayout.addWidget(self.list[self.num])
            self.num += 1
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
            
            self.trashBtnList[0].clicked.connect(self.delete_playlist)
            print(self.trashBtnList)
            if self.num == self.listLenth:
                break
