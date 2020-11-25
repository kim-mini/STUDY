from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic#form.ui를 읽어오기 위해서

from PyQt5.QtGui import *

form_class = uic.loadUiType("form.ui")[0]

class DigitalClock(QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        #self.label
        #self.lcdNumber
        #self.btn1

    def initUI(self):
        self.now = QDate.currentDate()
        col = QColor(0, 0, 0)
        self.setStyleSheet("background-color: %s"%col.name())#배경색 지정
        self.lcdNumber.setStyleSheet("color: white;")
        self.label.setStyleSheet("color: #505050;")
        self.btn1.setStyleSheet("color: white;"
                                "background-color: #505050")


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

        self.showTime()
        self.setWindowTitle("Digital Clock")
        #self.resize(800, 240)

        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(self.btnToggle)
        #self.btn.clicked.connect(self.CallTimer)  # 버튼을 누르면 함수호출


    def btnToggle(self):
        if self.btn1.isChecked():  # 버튼이 체크가 되어있다면 텍스트바꾸기
            col = QColorDialog.getColor()
            self.btn1.setText('Save')
            self.setStyleSheet("background-color: %s" % col.name())

        else:
            self.btn1.setText(self.now.toString('d.M.yy'))


    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        if (time.msec() > 500 ):
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        else:
            text = text

        self.lcdNumber.display(text)
    def CallTimer(self):
        pass

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
