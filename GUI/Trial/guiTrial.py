import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout,QPushButton,QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'ChatBot'
        self.statusMessage = 'Type your Message...'
        self.top = 300
        self.left = 1400
        self.height = 700
        self.width = 500
        self.initUI()  # next method call

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage(self.statusMessage)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App() #calls App class
    sys.exit(app.exec_())
