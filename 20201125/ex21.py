import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        self.text = QLabel('Hi',self)
        self.text.move(250,90)
        self.text.setFont(QFont('arial'))

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.change)
        self.dial.valueChanged.connect(self.change)


        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def change(self,value):
        self.slider.setValue(value)
        self.dial.setValue(value)
        self.text.setFont(QFont('arial', value))
        self.text.adjustSize()
    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())