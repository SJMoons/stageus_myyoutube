
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)

#         self.btn = QPushButton('Start', self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)

#         self.timer = QBasicTimer()
#         self.step = 0

#         self.setWindowTitle('QProgressBar')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()

#     def timerEvent(self, e):
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText('Finished')
#             return

#         self.step = self.step + 1
#         self.pbar.setValue(self.step)

#     def doAction(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())



    #     self.pbar = QProgressBar(self)
    #     self.pbar.setGeometry(30, 40, 200, 25)

    #     self.btn = QPushButton('Start', self)
    #     self.btn.move(40, 80)
    #     self.btn.clicked.connect(self.doAction)

    #     self.timer = QBasicTimer()
    #     self.step = 0

    #     self.setWindowTitle('QProgressBar')
    #     self.setGeometry(300, 300, 300, 200)
    #     self.show()

    # def timerEvent(self, e):
    #     if self.step >= 100:
    #         self.timer.stop()
    #         self.btn.setText('Finished')
    #         return

    #     self.step = self.step + 1
    #     self.pbar.setValue(self.step)

    # def doAction(self):
    #     if self.timer.isActive():
    #         self.timer.stop()
    #         self.btn.setText('Start')
    #     else:
    #         self.timer.start(100, self)
    #         self.btn.setText('Stop')




# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# class Ui:
#     def __init__(self):
       

#         # 메인윈도우 형성
#         self.mainWindow = QtWidgets.QMainWindow()
#         self.mainWindow.resize(1600,900)
#         self.mainWindow.setMinimumSize(QtCore.QSize(1600,600))
#         self.mainWindow.setMaximumSize(QtCore.QSize(1600,600))
#         self.mainWindow.setWindowTitle("YONGTUBE")
#         # 센트럴 위젯 형성
#         self.centralWidget = QtWidgets.QWidget(self.mainWindow)
#         self.centralWidget.setGeometry(0,0,1000,620)
#         self.centralWidget.setMinimumSize(QtCore.QSize(1600, 600))
#         self.centralWidget.setMaximumSize(QtCore.QSize(1600, 600)) 
#         # 스택위젯 형성
#         self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
#         self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 600))
#         self.stackedWidget.setMinimumSize(QtCore.QSize(1600, 600))
#         self.stackedWidget.setMaximumSize(QtCore.QSize(1600, 600))
#         self.stackedWidget.setStyleSheet("background-color : white;")

#     # 시작 페이지 0 
#         self.StartPage = QtWidgets.QWidget()
#         self.StartPage.setMinimumSize(QtCore.QSize(1600, 600))
#         self.StartPage.setMaximumSize(QtCore.QSize(1600, 600))
#         self.stackedWidget.addWidget(self.StartPage)

#         self.progressBar = QtWidgets.QProgressBar(self.StartPage)
#         self.progressBar.setGeometry(500,500,700,20)

#         self.btnStart = QtWidgets.QPushButton('Start')

#         self.mainWindow.show()
    #     self.scrollArea = QtWidgets.QScrollArea(self.StartPage)
    #     self.scrollArea.setGeometry(500,100,500,500)

    #     self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
    #     self.scrollAreaWidgetContents.setGeometry(0,0,500,800)

    #     self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        # self.result = QtWidgets.QDialog()
        # self.result.resize(300,100)
        # self.message = QtWidgets.QLabel(self.result) 
        # self.message.resize(100,20)
        # self.message.move(110,0)
        # self.message.setStyleSheet("font:13pt \"맑은 고딕\";")
        # self.message.setText("목록선택")
        # self.comboBox = QtWidgets.QComboBox(self.result)
        
        # self.comboBox.move(50,30)
        # self.comboBox.resize(200,30)
        # self.confirmBtn = QtWidgets.QPushButton(self.result)
        # self.confirmBtn.resize(100,30)
        # self.confirmBtn.move(95,65)
        # self.confirmBtn.setText("확인")
        # # print(str(self.comboBox.currentText())
        # # self.message.setAlignment(QtCore.Qt.AlignCenter)
        
        # self.result.show()
        # print(str(self.comboBox.currentText())
        # print(unicode(self.comboBox.currentText()))

    
    #     self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label)

    #     self.label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label2.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label2)
        
    #     self.label3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label3.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label3)
        
    #     self.label4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label4.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label4)


    #     self.label5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label5.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label5)

    #     self.label6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label6.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label6)
    #     self.label7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label7.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label7)
    #     self.label8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label8.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label8)
    #     self.label9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label9.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label9)
    #     self.label10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    #     self.label10.setStyleSheet("border:2px solid black;")
    #     self.verticalLayout.addWidget(self.label10)


    #     self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        



if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    main = Ui()
    sys.exit(app.exec_())