import PyQt5.QtWidgets as qtw

import MainUI

class Window(qtw.QMainWindow) :
    def __init__(self):
        #Call QMainWindow __init__
        super(Window, self).__init__()
        #Create internal ui
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        