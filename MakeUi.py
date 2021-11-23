from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MakeUi:
    def __init__(self):
        self.setpage = 0
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.setMinimumSize(QtCore.QSize(1600,900))
        self.mainWindow.setMaximumSize(QtCore.QSize(1600,900))
        self.mainWindow.resize(1600, 900)

        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0, 0, 1600, 900)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1600,900))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1600,900))
        self.stackedWidget.setStyleSheet("border: 15px solid black; background-color: white;")

        self.moonTube = QtWidgets.QPushButton(self.centralWidget)
        self.moonTube.setGeometry(60,45,420,120)
        self.moonTube.setStyleSheet("border:''; border-image: url(image/moontube.PNG);")
#setPixelsize
        #로그인 페이지 0
        self.login = QtWidgets.QWidget()  
        self.login.setGeometry(0, 0, 1600, 900)
        self.login.setStyleSheet("")

        self.loginNameText = QtWidgets.QLabel(self.login)
        self.loginNameText.setGeometry(605,55,411,111)
        self.loginNameText.setStyleSheet("font: 60pt \"맑은 고딕\";border: '';")
        self.loginNameText.setText("LOGIN")
        self.loginNameText.setAlignment(QtCore.Qt.AlignCenter)

        self.youtubeImage = QtWidgets.QLabel(self.login)
        self.youtubeImage.setGeometry(720,200,180,130)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        self.idWindow = QtWidgets.QLineEdit(self.login)
        self.idWindow.setGeometry(620, 370, 401, 71)
        self.idWindow.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black;")
        self.idWindow.setPlaceholderText("아이디")

        self.pwWindow = QtWidgets.QLineEdit(self.login)
        self.pwWindow.setGeometry(620, 460, 401, 71)
        self.pwWindow.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black;")
        self.pwWindow.setPlaceholderText("비밀번호")
        self.pwWindow.setEchoMode(2)

        self.loginBtn = QtWidgets.QPushButton(self.login)
        self.loginBtn.setGeometry(620,560,401,81)
        self.loginBtn.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black; background-color: #424242; color:white ;")
        self.loginBtn.setText("로그인")

        self.idpwFindList = []
        nameList = ["ID찾기","PW찾기"]
        for index in range(0,2):
            findingBtn = QtWidgets.QPushButton(self.login)
            xPos = 620 + (120*index)
            findingBtn.setGeometry(xPos,650,111,41)
            findingBtn.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black;")
            # findingBtn.setPixelsize(60)
            findingBtn.setText(nameList[index])
            self.idpwFindList.append(findingBtn)

        self.membershipBtn = QtWidgets.QPushButton(self.login)
        self.membershipBtn.setGeometry(890,650,130,41)
        self.membershipBtn.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black;")
        self.membershipBtn.setText("회원가입")

        self.stackedWidget.addWidget(self.login)

        #회원가입 페이지 1
        self.membership = QtWidgets.QWidget()
        self.membership.setGeometry(0,0,1600,900)

        self.idoverlapconfirm = QtWidgets.QPushButton(self.membership)
        self.idoverlapconfirm.setGeometry(1100, 170, 200, 71)
        self.idoverlapconfirm.setStyleSheet("font: 14pt \"맑은 고딕\"; background-color: lightgrey ; border: 1px solid black")
        self.idoverlapconfirm.setText("아이디 중복확인")

        self.exceptionIdPhoneList = []
        for index in range(0,2):
            exceptionIdPhone = QtWidgets.QTextBrowser(self.membership)
            xPos = 900 - (index*100)
            weight = 200 + (index*100)
            yPos = 135 + (index*475)
            exceptionIdPhone.setGeometry(xPos,yPos,weight,71)
            exceptionIdPhone.setStyleSheet("border: '';")
            self.exceptionIdPhoneList.append(exceptionIdPhone)

        self.exceptionPw = QtWidgets.QLabel(self.membership)
        self.exceptionPw.setGeometry(940,240,150,50)
        self.exceptionPw.setStyleSheet("border: '';")
        self.exceptionPw.setAlignment(QtCore.Qt.AlignCenter)

        nameList = ["아이디","비밀번호","부서/직급 ex)영업부/대리","이름","전화번호"]
        for index in range(0,5):
            membershipLabel = QtWidgets.QLabel(self.membership)
            yPos = 120 + (120*index)
            membershipLabel.setGeometry(540,yPos,240,40)
            membershipLabel.setStyleSheet("font:14pt \"맑은 고딕\"; border: '';")
            membershipLabel.setText(nameList[index])

        self.youtubeImage = QtWidgets.QPushButton(self.membership)
        self.youtubeImage.setGeometry(730,40,160,120)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        self.membershipList = []
        for index in range(0,5):
            memberinputLabel = QtWidgets.QLineEdit(self.membership)
            if index == 1:
                yPos = 170 + (118*index)
                memberinputLabel.setGeometry(540, yPos, 541, 71)
                memberinputLabel.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black;")
                memberinputLabel.setEchoMode(2)
                self.membershipList.append(memberinputLabel)
            else:
                yPos = 170 + (118*index)
                memberinputLabel.setGeometry(540, yPos, 541, 71)
                memberinputLabel.setStyleSheet("font:18pt \"맑은 고딕\"; border: 1px solid black;")
                self.membershipList.append(memberinputLabel)

        self.membershipmakepushbutton = QtWidgets.QPushButton(self.membership)
        self.membershipmakepushbutton.setGeometry(540, 740, 541, 71)
        self.membershipmakepushbutton.setStyleSheet("font: 18pt \"맑은 고딕\"; background-color: #424242; color: white; border: 1px solid black;")
        self.membershipmakepushbutton.setText("가입하기")

        self.gobackbutton = QtWidgets.QPushButton(self.membership)
        self.gobackbutton.setGeometry(1360,740,151,71)
        self.gobackbutton.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton.setText("뒤로 가기")

        self.stackedWidget.addWidget(self.membership)

        #아이디 찾기 페이지 2
        self.idfinding = QtWidgets.QWidget()

        self.youtubeImage = QtWidgets.QPushButton(self.idfinding)
        self.youtubeImage.setGeometry(730,40,160,120)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        nameList = ["이름","전화번호"]
        for index in range(0,2):
            namephoneLabel = QtWidgets.QLabel(self.idfinding)
            namephoneLabel.setStyleSheet("font:18pt \"맑은 고딕\"; border:'';")
            yPos = 190 + (index*180)
            namephoneLabel.setGeometry(550, yPos, 131, 51)
            namephoneLabel.setText(nameList[index])

        self.namephoneList = []
        for index in range(0,2):
            namephoneWindow = QtWidgets.QLineEdit(self.idfinding)
            yPos = 260 + (index*180)
            namephoneWindow.setStyleSheet("font:18pt \"맑은 고딕\"; border:1px solid black;")
            namephoneWindow.setGeometry(550,yPos,491,91)
            self.namephoneList.append(namephoneWindow)

        self.nextpushbutton1 = QtWidgets.QPushButton(self.idfinding)
        self.nextpushbutton1.setGeometry(QtCore.QRect(790, 570, 251, 81))
        self.nextpushbutton1.setStyleSheet("font: 18pt \"맑은 고딕\"; background-color: #424242; color: white; border: 1px solid black;")
        self.nextpushbutton1.setText("다음")

        self.gobackbutton1 = QtWidgets.QPushButton(self.idfinding)
        self.gobackbutton1.setGeometry(1360,740,151,71)
        self.gobackbutton1.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton1.setText("뒤로 가기")

        self.stackedWidget.addWidget(self.idfinding)

        #아이디 알려주는 페이지 3
        self.idprint = QtWidgets.QWidget()
        
        self.youtubeImage = QtWidgets.QPushButton(self.idprint)
        self.youtubeImage.setGeometry(730,40,160,120)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        self.idlistlabel = QtWidgets.QLabel(self.idprint)
        self.idlistlabel.setGeometry(515, 250, 721, 81)
        self.idlistlabel.setStyleSheet("font: 26pt \"맑은 고딕\"; border: '';")
        self.idlistlabel.setText("고객님의 정보와 일치하는 ID 목록입니다.")

        self.idrealprintlabel = QtWidgets.QTextBrowser(self.idprint)
        self.idrealprintlabel.setGeometry(620, 370, 401, 71)
        self.idrealprintlabel.setStyleSheet("background-color: rgb(251, 255, 224); font:20pt \"맑은 고딕\"; border:1px solid black;")
        
        self.gohomepushbutton = QtWidgets.QPushButton(self.idprint)
        self.gohomepushbutton.setGeometry(650, 500, 350, 55)
        self.gohomepushbutton.setStyleSheet("font: 15pt \"맑은 고딕\"; background-color: #424242; color: white; border:1px solid black;")
        self.gohomepushbutton.setText("로그인 화면으로 돌아가기")

        self.stackedWidget.addWidget(self.idprint)

        #비밀번호 찾기 페이지 4
        self.pwfinding = QtWidgets.QWidget()

        self.youtubeImage = QtWidgets.QPushButton(self.pwfinding)
        self.youtubeImage.setGeometry(730,40,160,120)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        nameList = ["아이디","전화번호"]
        for index in range(0,2):
            namephoneLabel = QtWidgets.QLabel(self.pwfinding)
            namephoneLabel.setStyleSheet("font:18pt \"맑은 고딕\"; border:'';")
            yPos = 190 + (index*180)
            namephoneLabel.setGeometry(550, yPos, 131, 51)
            namephoneLabel.setText(nameList[index])

        self.idphoneList = []
        for index in range(0,2):
            namephoneWindow = QtWidgets.QLineEdit(self.pwfinding)
            yPos = 260 + (index*180)
            namephoneWindow.setStyleSheet("font:18pt \"맑은 고딕\"; border:1px solid black;")
            namephoneWindow.setGeometry(550,yPos,491,91)
            self.idphoneList.append(namephoneWindow)

        self.gobackbutton2 = QtWidgets.QPushButton(self.pwfinding)
        self.gobackbutton2.setGeometry(1360,740,151,71)
        self.gobackbutton2.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton2.setText("뒤로 가기")

        self.nextpushbutton2 = QtWidgets.QPushButton(self.pwfinding)
        self.nextpushbutton2.setGeometry(790, 570, 251, 81)
        self.nextpushbutton2.setStyleSheet("font: 18pt \"맑은 고딕\"; background-color: #424242; color: white; border: 1px solid black;")
        self.nextpushbutton2.setText("다음")

        self.stackedWidget.addWidget(self.pwfinding)

        #새로운 비밀번호 만드는 페이지 5
        self.newpw = QtWidgets.QWidget()

        self.youtubeImage = QtWidgets.QPushButton(self.newpw)
        self.youtubeImage.setGeometry(730,40,160,120)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        self.newpwinputlabel = QtWidgets.QLabel(self.newpw)
        self.newpwinputlabel.setGeometry(540, 290, 541, 80)
        self.newpwinputlabel.setStyleSheet("font: 27pt \"맑은 고딕\"; border: '';")
        self.newpwinputlabel.setText("새로운 PW를 입력하세요.")
        self.newpwinputlabel.setAlignment(QtCore.Qt.AlignCenter)

        self.newpwrealinputlabel = QtWidgets.QLineEdit(self.newpw)
        self.newpwrealinputlabel.setGeometry(610, 400, 400, 60)
        self.newpwrealinputlabel.setStyleSheet("font:17pt \"맑은 고딕\"; border:1px solid black;")
        self.newpwrealinputlabel.setEchoMode(2)

        self.pwconfirmpushbutton = QtWidgets.QPushButton(self.newpw)
        self.pwconfirmpushbutton.setGeometry(630, 500, 350, 80)
        self.pwconfirmpushbutton.setStyleSheet("font: 15pt \"맑은 고딕\"; background-color: #424242; color: white; border:1px solid black;")
        self.pwconfirmpushbutton.setText("확인")

        self.stackedWidget.addWidget(self.newpw)

        #회원정보 및 수정 페이지 6
        self.memberShipInfor = QtWidgets.QWidget()

        self.inforLabel = QtWidgets.QLabel(self.memberShipInfor)
        self.inforLabel.setStyleSheet("border:''; font:26pt \"맑은 고딕\";")
        self.inforLabel.setGeometry(510,80,561,91)
        self.inforLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inforLabel.setText("회원님의 회원정보입니다")

        self.youtubeImage = QtWidgets.QLabel(self.memberShipInfor)
        self.youtubeImage.setGeometry(360,200,850,600)
        self.youtubeImage.setStyleSheet("border-image: url(image/youtube_logo.png);")

        nameList = ["아이디","부서/직급","이름","전화번호"]
        for index in range(0,4):
            InformLabel = QtWidgets.QLabel(self.memberShipInfor)
            yPos = 240 + (110*index)
            InformLabel.setGeometry(500,yPos,131,41)
            InformLabel.setStyleSheet("font:17pt \"맑은 고딕\"; border:''; color: white; background-color:'';")
            InformLabel.setText(nameList[index])

        self.informList = []
        for index in range(0,3):
            informList = QtWidgets.QLabel(self.memberShipInfor)
            yPos = 290 + (index*110)
            informList.setGeometry(500,yPos,161,51)
            informList.setStyleSheet("font:17pt \"맑은 고딕\"; border:1px solid black; background-color: white;")
            self.informList.append(informList)

        self.informList2 = QtWidgets.QLabel(self.memberShipInfor)
        self.informList2.setGeometry(500,620,200,51)
        self.informList2.setStyleSheet("font:17pt \"맑은 고딕\"; border:1px solid black; background-color: white;")

        self.memberDeleteBtn = QtWidgets.QPushButton(self.memberShipInfor)
        self.memberDeleteBtn.setGeometry(500,700,200,51)
        self.memberDeleteBtn.setStyleSheet("font:18pt\"맑은 고딕\"; border-image: url(image/button.png); color: white;")
        self.memberDeleteBtn.setText("계정 삭제")

        # self.idWindow.setPlaceholderText("아이디")
        nameList = ["아이디 수정","부서/직급 수정"]
        for index in range(0,2):
            updateInformLabel = QtWidgets.QLabel(self.memberShipInfor)
            yPos = 240 + (110*index)
            updateInformLabel.setGeometry(900,yPos,160,41)
            updateInformLabel.setStyleSheet("font:17pt \"맑은 고딕\"; border:''; color: white; background-color:'';")
            updateInformLabel.setText(nameList[index])

        self.updateList = []
        for index in range(0,2):
            updateIdDepart = QtWidgets.QLineEdit(self.memberShipInfor)
            yPos = 290 + (index*110)
            updateIdDepart.setGeometry(900,yPos,230,51)
            updateIdDepart.setStyleSheet("font:17pt \"맑은 고딕\"; border:1px solid black;")
            self.updateList.append(updateIdDepart)

        self.updateBtn = QtWidgets.QPushButton(self.memberShipInfor)
        self.updateBtn.setGeometry(930,480,170,51)
        self.updateBtn.setStyleSheet("font:18pt\"맑은 고딕\"; border-image: url(image/button.png); color: white;")
        self.updateBtn.setText("수정하기")

        self.gobackbutton3 = QtWidgets.QPushButton(self.memberShipInfor)
        self.gobackbutton3.setGeometry(1360,740,151,71)
        self.gobackbutton3.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton3.setText("뒤로 가기")

        self.stackedWidget.addWidget(self.memberShipInfor)

        #재생목록 페이지 7

        self.playListPage = QtWidgets.QWidget()

        self.memberId = QtWidgets.QLabel(self.playListPage)
        self.memberId.setGeometry(100,200,161,51)
        self.memberId.setStyleSheet("font:23pt \"맑은 고딕\"; border:1px solid black; background-color: rgb(251, 255, 224);")

        self.memberNameLabel = QtWidgets.QLabel(self.playListPage)
        self.memberNameLabel.setGeometry(280,200,140,51)
        self.memberNameLabel.setStyleSheet("font:17pt \"맑은 고딕\"; border:'';")
        self.memberNameLabel.setText("회원님")

        self.infoLogoutBtnList = []
        nameList = ["회원정보","로그아웃"]
        for index in range(0,2):
            infoLogoutBtn = QtWidgets.QPushButton(self.playListPage)
            yPos = 270 + (index*50)
            infoLogoutBtn.setGeometry(100,yPos,161,34)
            infoLogoutBtn.setStyleSheet("font:17pt \"맑은 고딕\"; border:1px solid black; color: white ; background-color: #424242;")
            infoLogoutBtn.setText(nameList[index])
            self.infoLogoutBtnList.append(infoLogoutBtn)

        self.makePlayList = QtWidgets.QPushButton(self.playListPage)
        self.makePlayList.setGeometry(100,370,200,65)
        self.makePlayList.setStyleSheet("font:18pt \"맑은 고딕\"; border-image: url(image/button.png); color: white ;")
        self.makePlayList.setText("재생목록 만들기")

        self.gobackbutton4 = QtWidgets.QPushButton(self.playListPage)
        self.gobackbutton4.setGeometry(100,700,151,71)
        self.gobackbutton4.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton4.setText("뒤로 가기")

        self.mainInputWindow = QtWidgets.QLineEdit(self.playListPage)
        self.mainInputWindow.setGeometry(580,70,880,65)
        self.mainInputWindow.setStyleSheet("font:19pt \"맑은 고딕\"; border: 1px solid black; ")

        self.searchBtn = QtWidgets.QPushButton(self.playListPage)
        self.searchBtn.setGeometry(1380,70,80,65)
        self.searchBtn.setStyleSheet("border-image: url(image/readingglass.jpeg); border: 2px solid black;")

        #재생목록박스
        
        self.scrollArea = QtWidgets.QScrollArea(self.playListPage)
        self.scrollArea.setGeometry(480,200,1050,600)
        # self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(900,65,900,900)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.addStretch()
        
        self.stackedWidget.addWidget(self.playListPage)

        #영상검색 페이지 8
        self.searchingPage = QtWidgets.QWidget()

        self.mainInputWindow2 = QtWidgets.QLineEdit(self.searchingPage)
        self.mainInputWindow2.setGeometry(580,70,880,65)
        self.mainInputWindow2.setStyleSheet("font:19pt \"맑은 고딕\"; border: 1px solid black; ")

        self.searchBtn2 = QtWidgets.QPushButton(self.searchingPage)
        self.searchBtn2.setGeometry(1380,70,80,65)
        self.searchBtn2.setStyleSheet("border-image: url(image/readingglass.jpeg); border: 1px solid black solid black;")
        
        self.gobackbutton5 = QtWidgets.QPushButton(self.searchingPage)
        self.gobackbutton5.setGeometry(1360,740,151,71)
        self.gobackbutton5.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton5.setText("뒤로 가기")

        #검색시 나오는 상위 5개
        self.videoThumbnailList = []
        for index in range(0,5):
            ThumbnailBox = QtWidgets.QLabel(self.searchingPage)
            yPos = 170 + (index*130)
            ThumbnailBox.setGeometry(660,yPos,200,121)
            
            self.videoThumbnailList.append(ThumbnailBox)

        self.videoBoxList = []
        for index in range(0,5):
            videoBox = QtWidgets.QLabel(self.searchingPage)
            yPos = 170 + (index*130)
            videoBox.setGeometry(660,yPos,681,121)
            videoBox.setStyleSheet("border: 1px solid black;")
            self.videoBoxList.append(videoBox)

        self.videoTitleList = []
        for index in range(0,5):
            videoTitle = QtWidgets.QLabel(self.searchingPage)
            yPos = 170 + (index*130)
            videoTitle.setGeometry(930,yPos,391,25)
            videoTitle.setStyleSheet("border: '';")
            self.videoTitleList.append(videoTitle)

        self.videoAuthorList = []
        for index in range(0,5):
            videoAuthor = QtWidgets.QLabel(self.searchingPage)
            yPos = 230 + (index*130)
            videoAuthor.setGeometry(930,yPos,241,25)
            videoAuthor.setStyleSheet("border:'';")
            self.videoAuthorList.append(videoAuthor)
    
        self.stackedWidget.addWidget(self.searchingPage)

        # 동영상 재생 페이지
        self.videoPlayPage = QtWidgets.QWidget()

        self.mainInputWindow3 = QtWidgets.QLineEdit(self.videoPlayPage)
        self.mainInputWindow3.setGeometry(580,70,880,65)
        self.mainInputWindow3.setStyleSheet("font:19pt \"맑은 고딕\"; border: 1px solid black; ")

        self.searchBtn3 = QtWidgets.QPushButton(self.videoPlayPage)
        self.searchBtn3.setGeometry(1380,70,80,65)
        self.searchBtn3.setStyleSheet("border-image: url(image/readingglass.jpeg); border: 1px solid black solid black;")

        self.gobackbutton6 = QtWidgets.QPushButton(self.videoPlayPage)
        self.gobackbutton6.setGeometry(50,700,151,71)
        self.gobackbutton6.setStyleSheet("font: 18pt \"맑은 고딕\"; color: white; border-image: url(image/button.png);")
        self.gobackbutton6.setText("뒤로 가기")

        
        self.stackedWidget.addWidget(self.videoPlayPage)
        self.mainWindow.show()

        
        # self.result = QtWidgets.QDialog()
        # self.result.resize(200,50)
        # self.message = QtWidgets.QLabel(self.result) 
        # self.message.resize(200,50)
        # self.message.move(0,0)
        # self.message = QtWidgets.QPushButton(self.result)

