from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui:
    def __init__(self):
        # 메인윈도우 형성
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1600,900)
        self.mainWindow.setMinimumSize(QtCore.QSize(1600,600))
        self.mainWindow.setMaximumSize(QtCore.QSize(1600,600))
        self.mainWindow.setWindowTitle("YONGTUBE")
        # 센트럴 위젯 형성
        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0,0,1000,620)
        self.centralWidget.setMinimumSize(QtCore.QSize(1600, 600))
        self.centralWidget.setMaximumSize(QtCore.QSize(1600, 600)) 
        # 스택위젯 형성
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 600))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1600, 600))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1600, 600))
        self.stackedWidget.setStyleSheet("background-color : white;")

    # 시작 페이지 0 
        self.StartPage = QtWidgets.QWidget()
        self.StartPage.setMinimumSize(QtCore.QSize(1600, 600))
        self.StartPage.setMaximumSize(QtCore.QSize(1600, 600))
        self.stackedWidget.addWidget(self.StartPage)
        
        self.scrollArea = QtWidgets.QScrollArea(self.StartPage)
        self.scrollArea.setGeometry(500,100,500,500)

        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(0,0,500,800)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

    


    
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label)

        self.label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label2.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label2)
        
        self.label3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label3.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label3)
        
        self.label4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label4.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label4)


        self.label5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label5.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label5)

        self.label6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label6.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label6)
        self.label7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label7.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label7)
        self.label8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label8.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label8)
        self.label9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label9.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label9)
        self.label10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label10.setStyleSheet("border:2px solid black;")
        self.verticalLayout.addWidget(self.label10)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        

        self.mainWindow.show()

if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    main = Ui()
    sys.exit(app.exec_())