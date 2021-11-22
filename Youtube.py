from pytchat import LiveChat            #검색창에 주소자체를 넣음 
import pafy
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

from PyQt5 import QtCore, QtGui, QtWidgets
import MakeUi
import threading
import time
import sys

class Youtube:
    def __init__(self,revui):
        self.ui = revui
        self.resultTitleList = []
        self.resultAuthorList = []
        self.resultViewList = []
        self.input = self.ui.mainInputWindow.text()
        self.ui.searchBtn.clicked.connect(self.init_event)

    def init_event(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 8)
        videoList = []
        DEVELOPER_KEY = "AIzaSyCAUDHrRl61GHr-14y2KHFndFANXsxdcso"
        YOUTUBE_API_SERVICE_NAME="youtube"
        YOUTUBE_API_VERSION="v3"
        self.youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
        search_response = self.youtube.search().list(
        q = self.input,
        order = "relevance",
        part = "snippet",
        maxResults = 8
        ).execute()
        # print(search_response)
        for item in search_response['items']:
            if item['id']['kind'] == 'youtube#video':
               videoList.append(item['id']['videoId'])

        for video in videoList:
            try:
                v = pafy.new(video)
                title = v.title
                author = v.author
                viewCount = v.viewcount
                self.resultTitleList.append(title)
                self.resultAuthorList.append(author)
                self.resultViewList.append(viewCount)
        
            except KeyError:
                pass
        self.video_view()
        
    def video_view(self):
        for index in range(0,5):
            self.ui.videoTitleList.setText(self.resultTitleList[index])
            self.ui.videoAuthorList.setText(self.resultAuthorList[index])

# if __name__ == '__main__':
#         youtube = Youtube()

class MyThread(threading.Thread, QtCore.QObject): 
    resultSignal = QtCore.pyqtSignal(str)   
    def __init__(self, revui):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self)

    def run(self):
        for video in videoList:
            try:
                v = pafy.new(video)
                title = v.title
                author = v.author
                viewCount = v.viewcount
                self.resultTitleList.append(title)
                self.resultAuthorList.append(author)
                self.resultViewList.append(viewCount)
        
            except KeyError:
                pass


# if __name__ == '__main__':
#         youtube = YouTube()

