from sqlite3.dbapi2 import Error
from pytchat import LiveChat            #검색창에 주소자체를 넣음 
import pafy
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets
import Config
import PlayListPage
import threading
import time
import sys

class Youtube:
    def __init__(self,revui,revdb,revplaylist):
        self.ui = revui
        self.db = revdb
        self.playList = revplaylist
        self.resultThumnailList = []
        self.resultTitleList = []
        self.resultAuthorList = []
        self.resultViewList = []
        self.videoList = []
        self.pList = []
        self.init_event()
        # self.input = self.ui.mainInputWindow.text()
    def init_event(self):
        self.ui.searchBtn.clicked.connect(self.search_event)     #이벤트가 실행된 후에 텍스트 실행되게해야 함
        self.ui.gobackbutton5.clicked.connect(self.goback_btn)
        for index in range(0,5):
            self.ui.videoAddBtnList[index].mousePressEvent = lambda event, num = index : self.video_input(event, num)

    def search_event(self):
        print("크롤링")
        self.input = self.ui.mainInputWindow.text()
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 8)
        DEVELOPER_KEY = "AIzaSyCAUDHrRl61GHr-14y2KHFndFANXsxdcso"
        YOUTUBE_API_SERVICE_NAME="youtube"
        YOUTUBE_API_VERSION="v3"
        self.youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
        search_response = self.youtube.search().list(
        q = self.input,
        order = "relevance",
        part = "snippet",
        maxResults = 12
        ).execute()
        # print(search_response)
        for item in search_response['items']:
            if item['id']['kind'] == 'youtube#video':
               self.videoList.append(item['id']['videoId'])

        for video in self.videoList:
            try:
                v = pafy.new(video)
                title = v.title
                author = v.author
                viewCount = v.viewcount
                self.thumbnail = v.thumb
                self.resultThumnailList.append(self.thumbnail)
                self.resultTitleList.append(title)
                self.resultAuthorList.append(author)
                self.resultViewList.append(viewCount)

            except (KeyError,ValueError,TypeError,OSError,Error):
                pass
        self.video_view()
        
    def video_view(self):
        # print(self.resultThumnailList[0])
        # print(self.resultThumnailList[1])
        # print(self.resultThumnailList[2])
        # print(self.resultThumnailList[3])
        # print(self.resultThumnailList[4])
        for index in range(0,5):
            image = urllib.request.urlopen(self.resultThumnailList[index]).read()
            pixmap = QtGui.QPixmap()
            self.ui.videoTitleList[index].setText(self.resultTitleList[index])
            self.ui.videoAuthorList[index].setText(self.resultAuthorList[index])
            self.ui.videoThumbnailList[index].setStyleSheet("border: 1px solid black;")
            pixmap.loadFromData(image)
            self.ui.videoThumbnailList[index].setPixmap(pixmap)

    def video_input(self, event, index):
        self.index = index
        # numberReset = self.playList.num
        self.all = self.db.cur.execute("SELECT * FROM playlist;")
        self.allPlayList = self.all.fetchall()
        self.a = 0
        while True:
            print("playlist")
            print(self.a)
            self.pList.append(self.allPlayList[self.playList.num-1][0])
            self.playList.num -= 1
            self.a+=1
            if self.playList.num == 0:
                self.playList.num = self.a 
                print(self.a)
                break
        self.window = Config.List()
        self.window.comboBox.addItems(self.pList)
        self.window.result.show()
        self.window.confirmBtn.clicked.connect(self.video_confirm)

    def video_confirm(self):
        print("hide")
        self.window.result.hide()
        self.pList = []
        self.db.create("playlistvideo",["playlist","video","title"],[self.window.comboBox.currentText(),"https://www.youtube.com/watch?v=" + self.videoList[self.index],self.resultTitleList[self.index]])

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 7)


# class MyThread(threading.Thread, QtCore.QObject): 
#     resultSignal = QtCore.pyqtSignal(str)   
#     def __init__(self, revui):
#         threading.Thread.__init__(self)
#         QtCore.QObject.__init__(self)

#     def run(self):
#         for video in videoList:
#             try:
#                 v = pafy.new(video)
#                 title = v.title
#                 author = v.author
#                 viewCount = v.viewcount
#                 self.resultTitleList.append(title)
#                 self.resultAuthorList.append(author)
#                 self.resultViewList.append(viewCount)
        
#             except KeyError:
#                 pass


# if __name__ == '__main__':
#         youtube = YouTube()

