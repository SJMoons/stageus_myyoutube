from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config

class PwFinding:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
        self.init_event()

    def init_event(self):
        self.ui.nextpushbutton2.clicked.connect(self.pwfind_nextbtn)
        self.ui.gobackbutton2.clicked.connect(self.goback_btn)


    def pwfind_nextbtn(self):
        self.idInput = self.ui.idphoneList[0].text()
        phonenumInput = self.ui.idphoneList[1].text()
        self.recvId = self.db.read("userinformation",["id"],[self.idInput])
        self.recvPhonenum = self.db.read("userinformation",["phonenum"],[phonenumInput])

        if  len(self.idInput) == 0 or len(phonenumInput) == 0 or len(self.recvId) == 0 or len(self.recvPhonenum) == 0:
            self.window = Config.Alert()
            self.window.message.setText("아이디와 전화번호를 확인해주세요")
            self.window.result.show()

        elif self.recvId[0][0] == self.recvPhonenum[0][0] :           
            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 5)
            self.newpw_inputlabel()

    def newpw_inputlabel(self):
        self.ui.pwconfirmpushbutton.clicked.connect(self.pwconfirm_btn)

    def pwconfirm_btn(self):
        self.newpwInput = self.ui.newpwrealinputlabel.text()             #버튼을 누른 후에 새로운 비밀번호 데이터를 가져와야 입력이 됨. 
        self.db.update("user",["pw"],[self.newpwInput],["id"],[self.idInput])
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)
        self.window = Config.Alert()
        self.window.message.setText("새 비밀번호로 변경되었습니다")
        self.window.result.show()

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)