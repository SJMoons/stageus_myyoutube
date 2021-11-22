from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config

class IdFinding:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
        self.init_event()

    def init_event(self):
        self.ui.nextpushbutton1.clicked.connect(self.idfind_nextbtn)
        self.ui.nextpushbutton1.enterEvent =lambda event: self.numberEnterEvent(event)
        self.ui.nextpushbutton1.leaveEvent =lambda event: self.numberLeaveEvent(event)
        self.ui.gobackbutton1.clicked.connect(self.goback_btn)
        self.ui.gobackbutton1.enterEvent =lambda event: self.numberEnterEvent1(event)
        self.ui.gobackbutton1.leaveEvent =lambda event: self.numberLeaveEvent1(event)
        self.ui.gohomepushbutton.clicked.connect(self.gohome_btn)
        self.ui.gohomepushbutton.enterEvent =lambda event: self.numberEnterEvent2(event)
        self.ui.gohomepushbutton.leaveEvent =lambda event: self.numberLeaveEvent2(event)

    def numberEnterEvent(self,event):
        self.ui.nextpushbutton1.setStyleSheet(
            "background-color: #212121;font: 18pt \"맑은 고딕\"; border-image: ''; color: white;"
        )

    def numberLeaveEvent(self,event):
        self.ui.nextpushbutton1.setStyleSheet(
            "background-color: #424242;font: 18pt \"맑은 고딕\"; border-image: ''; color: white;"
        )

    def numberEnterEvent1(self,event):
        self.ui.gobackbutton1.setStyleSheet(
            "background-color: #212121;font: 18pt \"맑은 고딕\"; border-image: ''; color: white;"
        )

    def numberLeaveEvent1(self,event):
        self.ui.gobackbutton1.setStyleSheet(
            "font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);"
        )

    def numberEnterEvent2(self,event):
        self.ui.gohomepushbutton.setStyleSheet(
            "background-color: #212121;font: 15pt \"맑은 고딕\"; border-image: ''; color: white;"
        )
    def numberLeaveEvent2(self,event):
        self.ui.gohomepushbutton.setStyleSheet(
            "background-color: #424242;font: 15pt \"맑은 고딕\"; border-image: ''; color: white;"
        )
    def idfind_nextbtn(self):
        nameInput = self.ui.namephoneList[0].text()
        phonenumInput = self.ui.namephoneList[1].text()
        self.recvName = self.db.read("userinformation",["name"],[nameInput])
        self.recvPhonenum = self.db.read("userinformation",["phonenum"],[phonenumInput])

        if  len(nameInput) == 0 or len(phonenumInput) == 0 or len(self.recvName) == 0 or len(self.recvPhonenum) == 0:
            self.window = Config.Alert()
            self.window.message.setText("이름과 전화번호를 확인해주세요")
            self.window.result.show()

        elif self.recvName[0][0] == self.recvPhonenum[0][0] :
            self.ui.nextpushbutton1.clicked.connect(self.idrealprint_label)

    def idrealprint_label(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 3)
        self.ui.idrealprintlabel.setText(self.recvName[0][0])
        self.ui.idrealprintlabel.setAlignment(QtCore.Qt.AlignCenter)

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def gohome_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)