import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl_red = QLabel('red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;" # 네모 윤곽선
                             "border-width: 2px;" # 선의 굵기
                             "border-color: #FA8072;" # 컬러
                             "border-radius: 5px")# 각의 둥글기
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4") # 윤곽선없이 색만채우기
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;" # 선
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())