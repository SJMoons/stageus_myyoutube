from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config

class VideoPlay:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 9)

        self.init_event()

    def init_event(self):
        self.ui.gobackbutton6.clicked.connect(self.goback_btn)



    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 7)
