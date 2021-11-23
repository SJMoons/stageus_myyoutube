from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Alert:    #Alert로 바꾸기        #파일이름바꾸기 Config
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

        self.confirm = QtWidgets.QPushButton(self.result)  #매개변수를 받아서
        self.confirm.setGeometry(103,50,100,20)
        self.confirm.setStyleSheet("font:8pt \"맑은 고딕\";")
        self.confirm.setText("확인")
        # self.confirm.clicked.connect(self.py.memberdelete_btn)

class Exception:
    def __init__(self):
        self.nameCheckList = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
        '1','2','3','4','5','6','7','8','9','0','ㅂ','ㅈ','ㄷ','ㄱ','ㅅ','ㅛ','ㅕ','ㅑ','ㅐ','ㅔ','ㅁ','ㄴ','ㅇ','ㄹ','ㅎ','ㅗ','ㅓ','ㅏ','ㅣ','ㅋ','ㅌ','ㅊ','ㅍ','ㅠ',\
        'ㅜ','ㅡ','ㅃ','ㅉ','ㄸ','ㄲ','ㅆ','ㅒ','ㅖ',
        ',','.','/',';',"'",'[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']
        
        self.departCheckList = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
        '1','2','3','4','5','6','7','8','9','0',
        ',','.',';',"'",'[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']

        self.phoneCheckList = ['ㅂ','ㅈ','ㄷ','ㄱ','ㅅ','ㅛ','ㅕ,''ㅑ','ㅐ','ㅔ','ㅁ','ㄴ','ㅇ','ㄹ','ㅎ','ㅗ','ㅓ','ㅏ','ㅣ','ㅋ','ㅌ','ㅊ','ㅍ','ㅠ','ㅜ','ㅡ',
        'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',',','.','/',';',"'",
        '[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']

        self.specialCharacterList = [',','.','/',';',"'",'[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']

        self.numberList = ['1','2','3','4','5','6','7','8','9','0']

        self.englishList = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

        self.koreanList = ['ㅂ','ㅈ','ㄷ','ㄱ','ㅅ','ㅛ','ㅕ,''ㅑ','ㅐ','ㅔ','ㅁ','ㄴ','ㅇ','ㄹ','ㅎ','ㅗ','ㅓ','ㅏ','ㅣ','ㅋ','ㅌ','ㅊ','ㅍ','ㅠ','ㅜ','ㅡ','ㅃ','ㅉ','ㄸ','ㄲ','ㅆ','ㅒ','ㅖ']


