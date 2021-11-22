from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config

class MemberInfo:     #클래스 나누기
    def __init__(self,revui,revdb,revmain):
        self.characterList2 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
        '1','2','3','4','5','6','7','8','9','0',
        ',','.',';',"'",'[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']
        self.main = revmain
        self.ui = revui
        self.db = revdb
        self.init_event()

    def init_event(self):
        self.ui.infoLogoutBtnList[0].clicked.connect(self.memberinfo_btn)
        self.ui.infoLogoutBtnList[1].clicked.connect(self.logout_btn)
        self.ui.memberDeleteBtn.clicked.connect(self.warning_btn)
        self.ui.updateBtn.clicked.connect(self.update_btn)
        self.ui.gobackbutton3.clicked.connect(self.goback_btn)
        self.ui.gobackbutton4.clicked.connect(self.goback_btn2)

    def memberinfo_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 6)
        self.recvResult1 = self.db.read("userinformation",["id"],[self.main.idValue])
        self.ui.informList[0].setText(self.recvResult1[0][0])
        self.ui.informList[1].setText(self.recvResult1[0][1])
        self.ui.informList[2].setText(self.recvResult1[0][2])
        self.ui.informList2.setText("0"+str(self.recvResult1[0][3]))

    def warning_btn(self):
        self.window = Config.Warning()
        self.window.confirm.clicked.connect(self.memberdelete_btn)
        self.window.message.setText("계정을 정말 삭제하시겠습니까?")
        self.window.result.show()

    def memberdelete_btn(self):
        print("1")
        self.db.delete("userinformation", ["id"], [self.main.idValue])
        self.db.delete("user",["id"], [self.main.idValue])
        self.window = Config.Alert()
        self.window.message.setText("계정이 삭제되었습니다.")
        self.window.result.show()
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def update_btn(self):
        updateId = self.ui.updateList[0].text()
        self.updateDepart = self.ui.updateList[1].text()
        confirmId = self.db.read("user",["id"],[updateId])
        if len(updateId) == 0 and len(self.updateDepart) == 0:
            self.window = Config.Alert()
            self.window.message.setText("'아이디'와 '부서/직급'을 입력해주세요.")
            self.window.result.show()

        elif len(confirmId) != 0:
            self.window = Config.Alert()
            self.window.message.setText("이미 있는 아이디입니다.")
            self.window.result.show()

        elif len(confirmId) == 0 and len(self.updateDepart) == 0 and len(updateId) != 0:
            self.db.update("userinformation", ["id"], [updateId], ["id"], [self.main.idValue])
            self.db.update("user",["id"],[updateId],["id"],[self.main.idValue])
            self.ui.informList[0].setText(updateId)
            self.window = Config.Alert()
            self.window.message.setText("아이디가 "+updateId+"로 수정되었습니다.")
            self.window.result.show()

        elif self.korean_check() and len(updateId) == 0 and len(self.updateDepart) != 0:
            self.db.update("userinformation", ["depart"], [self.updateDepart], ["id"], [self.main.idValue])
            self.ui.informList[1].setText(self.updateDepart)
            self.window = Config.Alert()
            self.window.message.setText("'부서/직급'이 "+self.updateDepart+"로 수정되었습니다.")
            self.window.result.show()
        
        elif self.korean_check() and len(updateId) != 0 and len(self.updateDepart) != 0 and len(confirmId) == 0:
            self.db.update("userinformation", ["id"], [updateId], ["id"], [self.main.idValue])
            self.db.update("user",["id"],[updateId],["id"],[self.main.idValue])
            self.db.update("userinformation", ["depart"], [self.updateDepart], ["id"], [self.main.idValue])
            self.ui.informList[0].setText(updateId)
            self.ui.informList[1].setText(self.updateDepart)
            self.window = Config.Alert()
            self.window.message.setText("'아이디'와 '부서/직급'이 수정되었습니다.")
            self.window.result.show()

    def korean_check(self):
        for index in range(0,len(list(self.updateDepart))):
            if self.updateDepart[index] in self.characterList2:
                self.window = Config.Alert()
                self.window.message.setText("부서/직급은 한글과 '/'만 사용가능합니다.")
                self.window.result.show()
                return False
        return True

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 7)

    def goback_btn2(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def logout_btn(self):
        exit()
