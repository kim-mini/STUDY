import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self)# push버튼 생성
      btn.move(110, 80) #버튼의 위치
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)
      # 버튼을 눌렀을 때 어떤 행동을 발생시킬 것인지
      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())