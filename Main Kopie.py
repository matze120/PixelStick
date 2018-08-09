import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import MainUI as App2
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 50
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        self.button = QPushButton("EXIT")
        pixmap = QPixmap('moon_splash.png')
        label.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height())
 
        self.show()
        self.button.clicked.connect(app.exit)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    App3 = App2.Ui_MainWindow()
    ex = App3()
    sys.exit(app.exec_())