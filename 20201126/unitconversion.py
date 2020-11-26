import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import math

form_class = uic.loadUiType("form.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.target = 0
        self.unit = 'mm'
        #self.label.setStyleSheet("color: #ffffff;")

    def initUI(self):
        self.col=QColor('white')#100,100,100)
        self.label.setStyleSheet("color: %s" % self.col.name())
        #print(self.col.name)
        #print(self.tab.)
        self.LenText.returnPressed.connect(self.textChanged)
        self.LenText.textChanged.connect(self.checkSTR)
        self.Ul.activated[str].connect(self.onActivated)

    def textChanged(self):
        # LenText에 있는 텍스트를 가져오는 메서드
        #object type = str

        targetSTR = self.LenText.text()
        self.target = float(targetSTR)
        self.convertUnit(self.target)


    def convertUnit(self,target):#변환해서 출력
        num = 0
        list=[0,1,2,3]
        changenum = 0

        if self.unit == 'mm':
            num = 1
        elif self.unit == 'cm':
            num = 2
        elif self.unit == 'm':
            num = 3
        elif self.unit == 'km':
            num = 4

        for i in list[:num]:
            changenum += i

        res = target*math.pow(10,changenum)# change -> mm
        self.Lentext1.setText(str(res))
        self.Lentext2.setText(str(res/10))
        self.Lentext3.setText(str(res/1000))
        self.Lentext4.setText(str(res/1000000))

    def onActivated(self,ulText):# combo widget
        self.unit = ulText
        self.convertUnit(self.target)

    def checkSTR(self):# 문자열을 입력받을 때 문자열 체크

        if self.LenText.text() == '00':
            self.LenText.setText('0')
        for j in range(len(self.LenText.text())):
            if self.LenText.text()[j].replace('.','').isalpha():
                self.col = QColor('gray')#99, 99, 99)
                self.label.setStyleSheet("color: %s" % self.col.name())
                self.LenText.setText(self.LenText.text()[:j])
            else :
                self.col = QColor('white')#100, 100, 100)
                self.label.setStyleSheet("color: %s" % self.col.name())

        if self.LenText.text().find('0') == 0:
            for i in range(0,10):
                if self.LenText.text().find(str(i)) == 1:
                    self.LenText.setText(self.LenText.text()[1:])
#                    print('t')
#                    print(self.LenText.text())

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()