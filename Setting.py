from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Setting:            #파일이름바꾸기 Config
    def __init__(self):
        self.result = QtWidgets.QDialog()
        self.result.resize(300,50)
        self.message = QtWidgets.QLabel(self.result) 
        self.message.resize(300,50)
        self.message.move(0,0)
        self.message.setStyleSheet("font:13pt \"맑은 고딕\";")
        self.message.setAlignment(QtCore.Qt.AlignCenter)

class Warning:
    def __init__(self):
        # self.py = PlayList.PlayList()
        self.result = QtWidgets.QDialog()
        self.result.resize(320,70)

        self.message = QtWidgets.QLabel(self.result)
        self.message.resize(300,70)
        self.message.move(0,0)
        self.message.setStyleSheet("font:13pt \"맑은 고딕\";")
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.confirm = QtWidgets.QPushButton(self.result)
        self.confirm.setGeometry(100,50,100,20)
        self.confirm.setStyleSheet("font:8pt \"맑은 고딕\";")
        self.confirm.setText("확인")
        # self.confirm.clicked.connect(self.py.memberdelete_btn)



