from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MakeUi
import MyDb
import IdFinding
import PlayList
import PwFinding
import MemberShip
import Setting

class Main:
    def __init__(self):
        self.ui = MakeUi.MakeUi()
        self.db = MyDb.MyDb()
        self.init_event()

    def init_event(self):
        self.ui.loginBtn.clicked.connect(self.login_btn)
        self.ui.loginBtn.enterEvent =lambda event: self.numberEnterEvent2(event)
        self.ui.loginBtn.leaveEvent =lambda event: self.numberLeaveEvent2(event)
        self.ui.idpwFindList[0].clicked.connect(self.idfind_btn)
        self.ui.idpwFindList[1].clicked.connect(self.pwfind_btn)
        for index in range(0,2):
            self.ui.idpwFindList[index].enterEvent =lambda event, num = index: self.numberEnterEvent(event, num)
            self.ui.idpwFindList[index].leaveEvent =lambda event, num = index: self.numberLeaveEvent(event, num)
        self.ui.membershipBtn.clicked.connect(self.membership_btn)
        self.ui.membershipBtn.enterEvent =lambda event: self.numberEnterEvent1(event)
        self.ui.membershipBtn.leaveEvent =lambda event: self.numberLeaveEvent1(event)


    def numberEnterEvent(self, event, index):
        self.ui.idpwFindList[index].setStyleSheet(
            "background-color: grey;font: 18pt \"맑은 고딕\"; border-image: '';"
        )
    def numberEnterEvent1(self, event):
        self.ui.membershipBtn.setStyleSheet(
            "background-color: grey;font: 18pt \"맑은 고딕\"; border-image: '';"
        )
    def numberEnterEvent2(self,event):
        self.ui.loginBtn.setStyleSheet(
            "font:18pt \"맑은 고딕\"; border-image: ''; background-color: #212121; color:white ;"
        )
    def numberLeaveEvent(self, event, index):
        self.ui.idpwFindList[index].setStyleSheet(
            "font: 18pt \"맑은 고딕\"; border-image: '';"
        )
    def numberLeaveEvent1(self,event):
        self.ui.membershipBtn.setStyleSheet(
            "font: 18pt \"맑은 고딕\"; border-image: '';"
        )
    def numberLeaveEvent2(self,event):
        self.ui.loginBtn.setStyleSheet(
            "font:18pt \"맑은 고딕\"; border-image: ''; background-color: #424242; color:white ;"
        )


    def login_btn(self):
        self.idValue = self.ui.idWindow.text()
        self.pwValue = self.ui.pwWindow.text()
        self.idResult = self.db.read("user",["id"],[self.idValue])
        self.pwResult = self.db.read("user",["pw"],[self.pwValue])
        if len(self.idResult) == 0 and len(self.pwResult) == 0:
            self.window = Setting.Setting()
            self.window.message.setText("ID와 PW를 확인해주세요")
            self.window.result.show()

        elif len(self.idResult) == 0:
            self.window = Setting.Setting()
            self.window.message.setText("ID를 확인해주세요")
            self.window.result.show()

        elif len(self.pwResult) == 0:
            self.window = Setting.Setting()
            self.window.message.setText("PW를 확인해주세요")
            self.window.result.show()

        else:
            self.playList = PlayList.PlayList(self.ui,self.db,main)
            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 7)
            self.ui.memberId.setText(self.idValue)
            self.ui.memberId.setAlignment(QtCore.Qt.AlignCenter)

    def idfind_btn(self):
        self.idFinding = IdFinding.IdFinding(self.ui,self.db)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 2)

    def pwfind_btn(self):
        self.pwFinding = PwFinding.PwFinding(self.ui,self.db)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 4)

    def membership_btn(self):
        self.memberShip = MemberShip.MemberShip(self.ui,self.db)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 1)



if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())