from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config
import VideoPlay
import sip

class PlayListPage:
    def __init__(self,revui,revdb):
        self.numCheckValue = 0
        self.numCheckValue2 = 0
        self.numCheckValue3 = 0
        self.num = 0
        self.list = []
        self.list2 = []
        self.trashBtnList = []
        self.trashBtnList2 = []
        self.playBtnList = []
        self.playBtnList2 = []
        self.ui = revui
        self.db = revdb
        getPlayList = self.db.read("playlist",["playlist"],[""])
        if len(getPlayList) == 0:
            self.all = self.db.cur.execute("SELECT * FROM playlist;")
            self.allPlayList = self.all.fetchall()
            self.listLenth = len(self.allPlayList)
            print(self.listLenth)
            if len(self.allPlayList) >0:
                self.exist_playlist()
                self._init__event()
            else:
                self._init__event()

    def _init__event(self):
        self.ui.makePlayList.clicked.connect(self.make_playlist)
        for index in range(0,self.listLenth):
            self.trashBtnList[index].mousePressEvent = lambda event, num = index : self.delete_event(event, num)
        for index in range(0,self.listLenth):
            self.playBtnList[index].mousePressEvent = lambda event, num = index : self.video_play(event, num)

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
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,(self.num*60))
            self.label = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
            self.label.setStyleSheet("border:1px solid black; background-color: lightgrey; font:18pt \"맑은 고딕\" ;")
            self.label.setText(playlistName)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setGeometry(0,0,500,50)
            self.label.setMaximumHeight(50)
            self.label.setMinimumHeight(50)
            
            for index in range(0,2):
                playtrashBtn = QtWidgets.QPushButton(self.label)
                xPos = 900 + (index*50)
                if index == 0:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/playbutton.jpg); border: '';")
                    self.playBtnList2.append(playtrashBtn)
                if index == 1:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/trashcanbutton.png); border: '';")
                    self.trashBtnList2.append(playtrashBtn)

            self.list2.append(self.label)
            self.ui.verticalLayout.addWidget(self.list2[self.numCheckValue3])
            self.num += 1
            self.numCheckValue3 += 1
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
            for index in range(0,self.num - self.listLenth):
                self.trashBtnList2[index].mousePressEvent = lambda event, num = index : self.delete_event2(event, num)
            for index2 in range(0,self.num - self.listLenth):
                self.playBtnList2[index2].mousePressEvent = lambda event, num = index : self.video_play(event, num)

    def delete_event(self, event, index):
        if self.numCheckValue == 0:
            self.num = self.num - 1
            self.num -= 1
            self.list[index].deleteLater()
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+((self.num)*60))
            self.numCheckValue += 1
            self.db.delete("playlist", ["playlist"], [self.list[index].text()])
            self.db.delete("playlistvideo",["playlist"],[self.list[index].text()])
        else:
            self.num -= 1
            self.list[index].deleteLater()
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+((self.num)*60))
            self.db.delete("playlist", ["playlist"], [self.list[index].text()])
            self.db.delete("playlistvideo",["playlist"],[self.list[index].text()])


    def delete_event2(self, event, index):
        print("ddd")
        if self.numCheckValue2 == 0:
            # index = index - 1
            # index -= 1
            # print(index)
            self.num = self.num - 1
            self.num -= 1
            self.list2[index].deleteLater()
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+((self.num)*60))
            self.numCheckValue2 += 1
            self.db.delete("playlist", ["playlist"], [self.list2[index].text()])
            self.db.delete("playlistvideo", ["playlist"], [self.list2[index].text()])
        else:
            self.num -= 1
            self.list2[index].deleteLater()
            self.ui.scrollAreaWidgetContents.setGeometry(0,0,1025,60+((self.num)*60))
            self.db.delete("playlist", ["playlist"], [self.list2[index].text()])
            self.db.delete("playlistvideo", ["playlist"], [self.list2[index].text()])


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
            
            for index in range(0,2):
                playtrashBtn = QtWidgets.QPushButton(self.label)
                xPos = 900 + (index*50)
                if index == 0:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/playbutton.jpg); border: '';")
                    self.playBtnList.append(playtrashBtn)
                if index == 1:
                    playtrashBtn.setGeometry(xPos,6,40,40)
                    playtrashBtn.setStyleSheet("border-image: url(image/trashcanbutton.png); border: '';")
                    self.trashBtnList.append(playtrashBtn)

            self.list.append(self.label)
            self.ui.verticalLayout.addWidget(self.list[self.num])
            self.num += 1
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)
           
            if self.num == self.listLenth:
                break

    def video_play(self,event,index):
        self.videoplay = VideoPlay.VideoPlay(self.ui,self.db,index,self.list,self.num)
        

            # self.videoPlay = VideoPlay.VideoPlay(self.ui,self.db)


# if len(self.getPlayList) == 0:
#             self.playListCount = 0
#         else:
#             self.playListCount = len(self.getPlayList)
#             for index in range(0,self.playListCount):
#                 self.scrollAreaWidgetContents.setGeometry(0,0,350,150+(self.playListCount*100))
#                 label  = QtWidgets.QLabel(self.scrollAreaWidgetContents)
#                 label.setStyleSheet("border : 2px solid black;")
#                 label.setMaximumHeight(100)
#                 label.setMinimumHeight(100)
#                 label.setMaximumWidth(300)
#                 label.setMinimumWidth(300)
#                 label.setText(self.getPlayList[index][1] + "\n"+"\n"+ self.getPlayList[index][2])
#                 label.setAlignment(QtCore.Qt.AlignTop)
#                 label.setAlignment(QtCore.Qt.AlignLeft)
                
#                 label.setStyleSheet("background-color : #D9D9D9;")
#                 label.setFont(self.getFont.videopage_playlist)
#                 self.playListList.append(label)

#                 self.button_play_playlist = QtWidgets.QPushButton(label)
#                 self.button_play_playlist.setStyleSheet("border-image : url(Pic/Play.png);")
