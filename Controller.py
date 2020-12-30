import Interface as GUI
import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
import prgElements as prg

class Controller() :
    def __init__(self,Argv):
        self.Argv = Argv

#    def MakeConnections(self):
#        self.Window.btnTest.clicked.connect(prgElements.writeToLog())        
        
    def run(self) : 
        self.App = qtw.QApplication(self.Argv)
        self.Window = GUI.Window()
        self.prog = prg.prgElement(self)
        self.MakeConnections()
        self.Window.show()
        self.start_timer()
        return self.App.exec_()

    def start_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.singleShot = False
        self.timer.setInterval(100)
        self.timer.start()
        self.timer.timeout.connect(self.checkGPIO)
 
    def MakeConnections(self):
        self.Window.ui.btnEnde.clicked.connect(self.exitSoftware)
        self.Window.ui.btnShutdown.clicked.connect(self.sysShutdown)
        self.Window.ui.btnRight.clicked.connect(self.incrListPos)
        self.Window.ui.btnLeft.clicked.connect(self.decrListPos)
        self.Window.ui.btnBrightInc.clicked.connect(self.incrBrightness)
        self.Window.ui.btnBrightDec.clicked.connect(self.decrBrightness)
        self.Window.ui.btnBrightIncFast.clicked.connect(self.incrBrightnessFast)
        self.Window.ui.btnBrightDecFast.clicked.connect(self.decrBrightnessFast)
        self.Window.ui.btnSpeedInc.clicked.connect(self.incrSpeed)
        self.Window.ui.btnSpeedDec.clicked.connect(self.decrSpeed)
        self.Window.ui.btnOK.clicked.connect(self.startScreensaver)
        self.Window.ui.btnFocus.clicked.connect(self.Focus)
        self.Window.ui.btnFocusOff.clicked.connect(self.FocusOff)
        self.Window.ui.btnFlOff.clicked.connect(self.LightOff)
        self.Window.ui.btnFl25.clicked.connect(self.Light25)
        self.Window.ui.btnFl50.clicked.connect(self.Light50)
        self.Window.ui.btnFl100.clicked.connect(self.Light100)
        
        
    def incrListPos(self):
        self.prog.incrListPos()
        
    def decrListPos(self):
        self.prog.decrListPos()
        
    def updatePixmap(self, val):
        self.Window.ui.labelImage.setPixmap(val)

    def incrBrightness(self):
        self.prog.incrBrightness(1)
        
    def decrBrightness(self):
        self.prog.decrBrightness(1)
        
    def incrBrightnessFast(self):
        self.prog.incrBrightness(10)
        
    def decrBrightnessFast(self):
        self.prog.decrBrightness(10)
    
    def updateBrightness(self, val):
        self.Window.ui.lcdBright.display(val)
        
    def incrSpeed(self):
        self.prog.incrSpeed()
        
    def decrSpeed(self):
        self.prog.decrSpeed()
        
    def updateSpeed(self, val):
        self.Window.ui.lcdSpeed.display(val)
        
    def updateTab(self, val):
        self.Window.ui.tabWidget.setCurrentIndex(val)
        
    def checkGPIO(self):
        self.prog.checkGPIO()
        
    def startScreensaver(self):
        self.prog.startScreensaver()

    def exitSoftware(self):
        self.prog.exitSoftware()
        
    def sysShutdown(self):
        self.prog.sysShutdown()
        
    def Focus(self):
        self.prog.focus()
        
    def FocusOff(self):
        self.prog.focusOff()
        
    def updateDuration(self, val):
        self.Window.ui.lblDuration.setText(str(val))
        
    def LightOff(self):
        self.prog.LightOff()
        
    def Light25(self):
        self.prog.Light(25)
        
    def Light50(self):
        self.prog.Light(50)
        
    def Light100(self):
        self.prog.Light(100)
        