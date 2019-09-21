import sys
from view import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,  parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.textEdit.textChanged.connect(self.calculate)
    
    def calculate(self):
        string = self.textEdit.toPlainText()
        length = len(string)
        flag = False
        charNum = 0
        wordNum = 0
        for i in range(0,  length):
            if((not flag) and string[i:i+1] != " "):
                flag = True
                wordNum += 1
            elif(flag and string[i:i+1] == " "):
                flag = False
            if(flag):
                charNum += 1
        self.wordNumberLabel.setText(str(wordNum))
        self.characterNumberLabel.setText(str(charNum))

if __name__=="__main__" :
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
