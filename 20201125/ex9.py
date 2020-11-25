import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)
        time = QTime.currentTime()
        now = QDate.currentDate()


        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel('Second Label', self)
        label3.setText(time.toString(Qt.DefaultLocaleShortDate))

        label4 = QLabel('Second Label', self)
        label4.setText(now.toString(Qt.ISODate))

        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)



        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())