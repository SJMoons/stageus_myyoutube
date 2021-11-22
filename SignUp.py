from os import name
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Config

class SignUp:   #Signup 파일이름도
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db= revdb
        self.ui.membershipList[0].textChanged.connect(self.onChanged)
        self.ui.membershipList[4].textChanged.connect(self.onChanged)
        self.ui.membershipList[1].textChanged.connect(self.security_result)
        self.init_event()
        self.exceptionCheck = Config.Exception()
        
    def init_event(self):
        self.ui.membershipmakepushbutton.clicked.connect(self.membership_makebutton)
        self.ui.idoverlapconfirm.clicked.connect(self.membership_idbtn)
        self.ui.gobackbutton.clicked.connect(self.goback_btn)
        self.idcheck = 0

    def membership_idbtn(self):
        self.idcheck += 1
        self.idInput = self.ui.membershipList[0].text()
        self.recvId = self.db.read("userinformation",["id"],[self.idInput])

        if  len(self.recvId) > 0:
            self.window = Config.Alert()
            self.window.message.setText("사용하실 수 없는 아이디입니다")
            self.window.result.show()

        elif len(list(self.idInput)) >9:
            self.window = Config.Alert()
            self.window.message.setText("아이디 길이가 초과되었습니다.")
            self.window.result.show()

        elif len(self.idInput) == 0:
            self.window = Config.Alert()
            self.window.message.setText("아이디를 적어주세요")
            self.window.result.show()

        else:
            self.window = Config.Alert()
            self.window.message.setText("사용하실 수 있는 아이디입니다")
            self.window.result.show()
            self.ui.membershipList[0].setDisabled(True)  #아이디 입력 막기

    def membership_makebutton(self):
        self.idInput = self.ui.membershipList[0].text()
        self.pwInput = self.ui.membershipList[1].text()
        self.departInput = self.ui.membershipList[2].text()
        self.nameInput = self.ui.membershipList[3].text()
        self.phonenumInput = self.ui.membershipList[4].text()
        phonenumList = self.db.read("userinformation",["phonenum"],[self.phonenumInput])

        if len(self.idInput) == 0 :
            self.window = Config.Alert()
            self.window.message.setText("아이디를 적어주세요")
            self.window.result.show()

        elif len(list(self.idInput)) >9:
            self.window = Config.Alert()
            self.window.message.setText("아이디 길이가 초과되었습니다.")
            self.window.result.show()

        elif len(self.pwInput) == 0:
            self.window = Config.Alert()
            self.window.message.setText("비밀번호를 적어주세요")
            self.window.result.show()

        elif self.korean_check():
            pass

        elif self.security_check() == 3:
            self.window = Config.Alert()
            self.window.message.setText("비밀번호의 보안성이 너무 낮습니다.")
            self.window.result.show()

        elif len(self.departInput) == 0:
            self.window = Config.Alert()
            self.window.message.setText("부서와 직급을 적어주세요")
            self.window.result.show()

        elif self.role_check():
            pass

        elif len(self.nameInput) == 0:
            self.window = Config.Alert()
            self.window.message.setText("이름을 적어주세요")
            self.window.result.show()
        
        elif self.name_check():
            pass


        elif len(self.phonenumInput) == 0:
            self.window = Config.Alert()
            self.window.message.setText("전화번호를 적어주세요")
            self.window.result.show()

        elif  1 <= len(list(self.phonenumInput)) <= 9 or 11 < len(list(self.phonenumInput)):
            self.window = Config.Alert()
            self.window.message.setText("전화번호는 10자리에서 11자리까지 가능합니다.")
            self.window.result.show()

        elif self.phone_check():
            pass

        elif len(phonenumList) > 0:
            self.window = Config.Alert()
            self.window.message.setText("이미 있는 전화번호입니다.")
            self.window.result.show()

        elif self.idcheck == 0:
            self.window = Config.Alert()
            self.window.message.setText("아이디 중복체크를 해주세요")
            self.window.result.show()

        elif len(self.recvId) > 0:
            self.window = Config.Alert()
            self.window.message.setText("사용하실 수 없는 아이디입니다.")
            self.window.result.show()

        else:                    
            self.db.create("user",["id","pw"],[self.idInput,self.pwInput])
            self.db.create("userinformation",["id","depart","name","phonenum"],[self.idInput,self.departInput,self.nameInput,self.phonenumInput])
            self.window = Config.Alert()
            self.window.message.setText("회원가입이 완료되었습니다 감사합니다")
            self.window.result.show()
            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def name_check(self):         #함수 이름 바꾸기 namecheck
        for index in range(0,len(list(self.nameInput))):
            if self.nameInput[index] in self.exceptionCheck.nameCheckList:
                self.window = Config.Alert()
                self.window.message.setText("이름은 한글과 완전한 음절만 사용가능합니다")
                self.window.result.show()
                return True
        return False

    def role_check(self):    #role check
        for index in range(0,len(list(self.departInput))):
            if self.departInput[index] in self.exceptionCheck.departCheckList:
                self.window = Config.Alert()
                self.window.message.setText("부서/직급은 한글과 '/'만 사용가능합니다")
                self.window.result.show()
                return True
        return False

    def phone_check(self):
        for index in range(0,len(list(self.phonenumInput))):
            if self.phonenumInput[index] in self.exceptionCheck.phoneCheckList:
                self.window = Config.Alert()
                self.window.message.setText("전화번호는 숫자만 사용가능합니다")
                self.window.result.show()
                return True
        return False

    def korean_check(self):
        for index in range(0,len(list(self.pwInput))):
            if self.pwInput[index] in self.exceptionCheck.koreanList:
                self.window = Config.Alert()
                self.window.message.setText("비밀번호는 영어와 특수문자만 가능합니다.")
                self.window.result.show()
                return True
        return False

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def onChanged(self):
        if len(list(self.ui.membershipList[0].text())) > 9:
            self.ui.exceptionIdPhoneList[0].setStyleSheet("color:red; border: ''; font: 10pt \"맑은 고딕\";")
            self.ui.exceptionIdPhoneList[0].setText("아이디의 길이가 너무 깁니다.")

        elif 1<=len(list(self.ui.membershipList[0].text())) <= 8:
            self.ui.exceptionIdPhoneList[0].setStyleSheet("color:green;  border: ''; font: 10pt \"맑은 고딕\";")
            self.ui.exceptionIdPhoneList[0].setText("사용할 수 있는 길이입니다")

        elif len(list(self.ui.membershipList[0].text())) == 0:
               self.ui.exceptionIdPhoneList[0].setText("")

        if len(list(self.ui.membershipList[4].text())) == 10 or len(list(self.ui.membershipList[4].text())) == 11 or len(list(self.ui.membershipList[4].text())) == 0:
            self.ui.exceptionIdPhoneList[1].setText("")

        else:            
            self.ui.exceptionIdPhoneList[1].setStyleSheet("color:red;  border: ''; font: 10pt \"맑은 고딕\";")
            self.ui.exceptionIdPhoneList[1].setText("전화번호는 10자리에서 11자리까지 가능합니다.")

    def pw_charactercheck(self, characterList):
        self.pwList = self.ui.membershipList[1].text()
        for index in range(0,len(list(self.pwList))):
            if self.pwList[index] in characterList:
                return True
        return False

    def security_check(self):
            checkSec = 0
            if self.pw_charactercheck(self.exceptionCheck.numberList):
                checkSec += 1

            if self.pw_charactercheck(self.exceptionCheck.englishList):
                checkSec += 1

            if self.pw_charactercheck(self.exceptionCheck.specialCharacterList):
                checkSec += 1

            if self.pw_charactercheck(self.exceptionCheck.koreanList):
                checkSec += 10
            return checkSec
            
    def security_result(self):
            if self.security_check() == 0:
                self.ui.exceptionPw.setText("")

            if self.security_check() == 3:
                self.ui.exceptionPw.setStyleSheet("color:green;  border: ''; font: 10pt \"맑은 고딕\";")
                self.ui.exceptionPw.setText("보안성 좋음")

            if self.security_check() == 2:
                self.ui.exceptionPw.setStyleSheet("color:black;  border: ''; font: 10pt \"맑은 고딕\";")
                self.ui.exceptionPw.setText("보안성 보통")

            if self.security_check() == 1:
                self.ui.exceptionPw.setStyleSheet("color:red;  border: ''; font: 10pt \"맑은 고딕\";")
                self.ui.exceptionPw.setText("보안성 낮음")

            if self.security_check() >=10:
                self.ui.exceptionPw.setStyleSheet("color:red;  border: ''; font: 10pt \"맑은 고딕\";")
                self.ui.exceptionPw.setText("한글은 사용불가합니다")