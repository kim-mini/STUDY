import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDesktopWidget


class MyApp(QWidget):

    def __init__(self):# 클래스가 선언이되면 자동실행
        super().__init__()# 부모클래스(QWidget)초기화도 해준다
        self.initUI()# MyApp 클래스 초기화

    def initUI(self):
        self.setWindowTitle('My First Application')#창이름
        self.center()
        self.resize(400, 200)
        self.show()

    def center(self):
        frame_info = self.frameGeometry()
        print(f'-> frame_info : {frame_info}')
        display_center = QDesktopWidget().availableGeometry().center()
        print(f'-> display_center : {display_center}')
        frame_info.moveCenter(display_center)
        self.move(frame_info.topLeft())


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())