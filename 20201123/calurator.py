import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




class Button(QToolButton):#push button 설정
    def __init__(self, text, Bcolor, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.BntColor(Bcolor)
        self.setFont(QFont('Apple SD Gothic Neo', 20))

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 50)
        size.setWidth(max(size.width(), size.height()))

        return size

    def BntColor(self,Bcolor):
        button = super(Button, self)

        if Bcolor == 1:# 숫자
            button.setStyleSheet("color: #363636;"                               
                                 "border-style: solid;"                              
                                 "border-width: 0.5px;"
                                 "border-color: #363636;"
                                 "background-color: #C9C9C9")
        elif Bcolor == 2:# 사칙연산
            button.setStyleSheet("color: white;"
                                 "border-style: solid;"
                                 "border-width: 0.5px;"
                                 "border-color: #363636;"
                                 "background-color: #FFA500")
        elif Bcolor == 3:# 맨윗줄
            button.setStyleSheet("color: #363636;"
                                 "border-style: solid;"
                                 "border-width: 0.5px;"
                                 "border-color: #363636;"
                                 "background-color: #A6A6A6")


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def createButton(self, text, BnC):
        button = Button(text, BnC)
        return button



    def initUI(self):
        #배경색 지정
        self.setStyleSheet("background-color: #363636")
        self.grid = QGridLayout()
        self.grid.setSpacing(0) #padding 값
        self.setLayout(self.grid)

        self.display = QLineEdit('2')#계산기의 숫자를 보여줌
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)# 오른쪽 정렬
        self.display.setMaxLength(5)#글자제한
        #계산이 출력되는 부분 폰트설정
        font = self.display.font()
        font.setPointSize(font.pointSize() + 25)
        self.display.setFont(font)
        self.display.setStyleSheet("color: white;")

        # 버튼생성
        btn1 = self.createButton('AC',3)
        btn2 = self.createButton('+/-',3)
        btn3 = self.createButton('%',3)
        btn4 = self.createButton('÷',2)
        btn5 = self.createButton('7',1)
        btn6 = self.createButton('8',1)
        btn7 = self.createButton('9',1)
        btn8 = self.createButton('X',2)
        btn9 = self.createButton('4',1)
        btn10 = self.createButton('5',1)
        btn11 = self.createButton('6',1)
        btn12 = self.createButton('-',2)
        btn13 = self.createButton('1',1)
        btn14 = self.createButton('2',1)
        btn15 = self.createButton('3',1)
        btn16 = self.createButton('+',2)
        btn17 = self.createButton('0',1)
        btn18 = self.createButton('.',1)
        btn19 = self.createButton('=',2)

        #self.btn1.pressed.connect(self.clear_text)


        #버튼의 레이아웃
        self.grid.addWidget(self.display, 0, 0,1,4)
        self.grid.addWidget(btn1, 2, 0)
        self.grid.addWidget(btn2, 2, 1)
        self.grid.addWidget(btn3, 2, 2)
        self.grid.addWidget(btn4, 2, 3)
        self.grid.addWidget(btn5, 3, 0)
        self.grid.addWidget(btn6, 3, 1)
        self.grid.addWidget(btn7, 3, 2)
        self.grid.addWidget(btn8, 3, 3)
        self.grid.addWidget(btn9, 4, 0)
        self.grid.addWidget(btn10, 4, 1)
        self.grid.addWidget(btn11, 4, 2)
        self.grid.addWidget(btn12, 4, 3)
        self.grid.addWidget(btn13, 5, 0)
        self.grid.addWidget(btn14, 5, 1)
        self.grid.addWidget(btn15, 5, 2)
        self.grid.addWidget(btn16, 5, 3)
        self.grid.addWidget(btn17, 6, 0, 1, 2)
        self.grid.addWidget(btn18, 6, 2)
        self.grid.addWidget(btn19, 6, 3)

        self.setWindowTitle('Calcurator')
        self.setGeometry(300, 300, 300, 500)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())