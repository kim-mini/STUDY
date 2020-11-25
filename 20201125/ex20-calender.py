import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from quickstart import *



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.datelist = []
        self.timelist = []
        self.eventlist = []

    def initUI(self):
        # google calender API
        self.datelist,self.timelist,self.eventlist = readGoogleCal()
        #print(datelist)
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)





        self.lbl = QTextEdit(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        self.calText = QTextEdit()
        self.calText.setText("")
        self.calText.clear()

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.calText)


        self.setLayout(vbox)

        self.setWindowTitle('miniCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()
        #print(date.toString(Qt.ISODate),datelist[0])
        print(eventlist)



    def showDate(self, date):


        self.lbl.setText(date.toString())
        self.calText.setText("")

        for i in range(len(datelist)) :#date가 겹친다면 일정을 출력하도록 한다
            if date.toString(Qt.ISODate) == datelist[i]:
                print(date,datelist[i],eventlist[i])
                text = self.calText.toPlainText()
                self.calText.setText(date.toString()+text+'\n'+' ' + timelist[i] + ' ' + eventlist[i])

    def clear_text(self):
        self.calText.clear()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())