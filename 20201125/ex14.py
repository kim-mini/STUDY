import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('&power on', self)
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(self.btnToggle)#클릭이되면

        self.btn2 = QPushButton(self)
        self.btn2.setText('Button&2')

        self.btn3 = QPushButton('Button3', self)
        self.btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def btnToggle(self):
        if self.btn1.isChecked():#버튼이 체크가 되어있다면 텍스트바꾸기
            self.btn1.setText('power off')
        else :
            self.btn1.setText('power on')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())