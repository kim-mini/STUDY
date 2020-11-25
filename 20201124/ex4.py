import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))# 툴팁의 폰트,폰트사이즈 지정
        self.setToolTip('This is a <b>QWidget</b> widget')# 툴팁 내용

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')# 버튼툴팁설정
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())