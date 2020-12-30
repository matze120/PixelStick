# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 321, 201))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.normal = QtWidgets.QWidget()
        self.normal.setObjectName("normal")
        self.labelImage = QtWidgets.QLabel(self.normal)
        self.labelImage.setGeometry(QtCore.QRect(60, 0, 170, 170))
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.btnLeft = QtWidgets.QPushButton(self.normal)
        self.btnLeft.setGeometry(QtCore.QRect(0, 60, 51, 32))
        self.btnLeft.setObjectName("btnLeft")
        self.btnOK = QtWidgets.QPushButton(self.normal)
        self.btnOK.setGeometry(QtCore.QRect(0, 150, 51, 32))
        self.btnOK.setObjectName("btnOK")
        self.btnRight = QtWidgets.QPushButton(self.normal)
        self.btnRight.setGeometry(QtCore.QRect(240, 60, 51, 32))
        self.btnRight.setObjectName("btnRight")
        self.tabWidget.addTab(self.normal, "")
        self.menu = QtWidgets.QWidget()
        self.menu.setObjectName("menu")
        self.btnSpeedInc = QtWidgets.QPushButton(self.menu)
        self.btnSpeedInc.setGeometry(QtCore.QRect(240, 10, 41, 41))
        self.btnSpeedInc.setObjectName("btnSpeedInc")
        self.btnBrightInc = QtWidgets.QPushButton(self.menu)
        self.btnBrightInc.setGeometry(QtCore.QRect(190, 60, 41, 41))
        self.btnBrightInc.setObjectName("btnBrightInc")
        self.btnBrightDec = QtWidgets.QPushButton(self.menu)
        self.btnBrightDec.setGeometry(QtCore.QRect(60, 60, 41, 41))
        self.btnBrightDec.setObjectName("btnBrightDec")
        self.btnSpeedDec = QtWidgets.QPushButton(self.menu)
        self.btnSpeedDec.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.btnSpeedDec.setObjectName("btnSpeedDec")
        self.lcdSpeed = QtWidgets.QLCDNumber(self.menu)
        self.lcdSpeed.setGeometry(QtCore.QRect(115, 20, 64, 31))
        self.lcdSpeed.setObjectName("lcdSpeed")
        self.lcdBright = QtWidgets.QLCDNumber(self.menu)
        self.lcdBright.setGeometry(QtCore.QRect(115, 70, 64, 31))
        self.lcdBright.setObjectName("lcdBright")
        self.btnBrightIncFast = QtWidgets.QPushButton(self.menu)
        self.btnBrightIncFast.setGeometry(QtCore.QRect(240, 60, 41, 41))
        self.btnBrightIncFast.setObjectName("btnBrightIncFast")
        self.btnBrightDecFast = QtWidgets.QPushButton(self.menu)
        self.btnBrightDecFast.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.btnBrightDecFast.setObjectName("btnBrightDecFast")
        self.lblDuration = QtWidgets.QLabel(self.menu)
        self.lblDuration.setGeometry(QtCore.QRect(220, 110, 41, 16))
        self.lblDuration.setObjectName("lblDuration")
        self.label = QtWidgets.QLabel(self.menu)
        self.label.setGeometry(QtCore.QRect(260, 110, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.menu)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 91, 16))
        self.label_2.setObjectName("label_2")
        self.btnRL = QtWidgets.QPushButton(self.menu)
        self.btnRL.setGeometry(QtCore.QRect(190, 150, 91, 32))
        self.btnRL.setObjectName("btnRL")
        self.btnLR = QtWidgets.QPushButton(self.menu)
        self.btnLR.setGeometry(QtCore.QRect(10, 150, 91, 32))
        self.btnLR.setObjectName("btnLR")
        self.tabWidget.addTab(self.menu, "")
        self.tools = QtWidgets.QWidget()
        self.tools.setObjectName("tools")
        self.btnFocus = QtWidgets.QPushButton(self.tools)
        self.btnFocus.setGeometry(QtCore.QRect(200, 10, 81, 32))
        self.btnFocus.setObjectName("btnFocus")
        self.btnFocusOff = QtWidgets.QPushButton(self.tools)
        self.btnFocusOff.setGeometry(QtCore.QRect(200, 50, 81, 32))
        self.btnFocusOff.setObjectName("btnFocusOff")
        self.btnFlOff = QtWidgets.QPushButton(self.tools)
        self.btnFlOff.setGeometry(QtCore.QRect(10, 130, 91, 32))
        self.btnFlOff.setObjectName("btnFlOff")
        self.btnFl100 = QtWidgets.QPushButton(self.tools)
        self.btnFl100.setGeometry(QtCore.QRect(10, 90, 91, 32))
        self.btnFl100.setObjectName("btnFl100")
        self.btnFl50 = QtWidgets.QPushButton(self.tools)
        self.btnFl50.setGeometry(QtCore.QRect(10, 50, 91, 32))
        self.btnFl50.setObjectName("btnFl50")
        self.btnFl25 = QtWidgets.QPushButton(self.tools)
        self.btnFl25.setGeometry(QtCore.QRect(10, 10, 91, 32))
        self.btnFl25.setObjectName("btnFl25")
        self.label_3 = QtWidgets.QLabel(self.tools)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 171, 16))
        self.label_3.setObjectName("label_3")
        self.btnShutdown = QtWidgets.QPushButton(self.tools)
        self.btnShutdown.setGeometry(QtCore.QRect(190, 140, 91, 32))
        self.btnShutdown.setObjectName("btnShutdown")
        self.btnEnde = QtWidgets.QPushButton(self.tools)
        self.btnEnde.setGeometry(QtCore.QRect(190, 100, 91, 32))
        self.btnEnde.setObjectName("btnEnde")
        self.tabWidget.addTab(self.tools, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PixelStick Controller"))
        self.btnLeft.setText(_translate("MainWindow", "<-"))
        self.btnOK.setText(_translate("MainWindow", "OK"))
        self.btnRight.setText(_translate("MainWindow", "->"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.normal), _translate("MainWindow", "Use"))
        self.btnSpeedInc.setText(_translate("MainWindow", "+"))
        self.btnBrightInc.setText(_translate("MainWindow", "+"))
        self.btnBrightDec.setText(_translate("MainWindow", "-"))
        self.btnSpeedDec.setText(_translate("MainWindow", "-"))
        self.btnBrightIncFast.setText(_translate("MainWindow", "+ +"))
        self.btnBrightDecFast.setText(_translate("MainWindow", "- -"))
        self.lblDuration.setText(_translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "s"))
        self.label_2.setText(_translate("MainWindow", "Anzeigedauer:"))
        self.btnRL.setText(_translate("MainWindow", "R -> L"))
        self.btnLR.setText(_translate("MainWindow", "L -> R"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.menu), _translate("MainWindow", "Menu"))
        self.btnFocus.setText(_translate("MainWindow", "FocusOn"))
        self.btnFocusOff.setText(_translate("MainWindow", "FocusOff"))
        self.btnFlOff.setText(_translate("MainWindow", "Light Off"))
        self.btnFl100.setText(_translate("MainWindow", "Light 100%"))
        self.btnFl50.setText(_translate("MainWindow", "Light 50%"))
        self.btnFl25.setText(_translate("MainWindow", "Light 25%"))
        self.label_3.setText(_translate("MainWindow", "(c) matze120 2018 - 2020"))
        self.btnShutdown.setText(_translate("MainWindow", "Shutdown"))
        self.btnEnde.setText(_translate("MainWindow", "Ende"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools), _translate("MainWindow", "Tools"))

