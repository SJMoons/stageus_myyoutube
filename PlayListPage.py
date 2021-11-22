from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config

class PlayListPage:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
        self.input = self.ui.mainInputWindow.text()
        self._init__event()

    def _init__event(self):
        self.ui.searchBtn.clicked.connect(self.search_event)



    def search_event(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 8)
