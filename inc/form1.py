# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inc/form1.ui'
#
# Created: Tue Apr 14 20:36:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(800, 600)
        mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 90, 781, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 781, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tableWidgetAccounts = QtGui.QTableWidget(self.centralwidget)
        self.tableWidgetAccounts.setEnabled(True)
        self.tableWidgetAccounts.setGeometry(QtCore.QRect(10, 190, 391, 341))
        self.tableWidgetAccounts.setObjectName(_fromUtf8("tableWidgetAccounts"))
        self.tableWidgetAccounts.setColumnCount(0)
        self.tableWidgetAccounts.setRowCount(0)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 203, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelSeed1 = QtGui.QLabel(self.layoutWidget)
        self.labelSeed1.setObjectName(_fromUtf8("labelSeed1"))
        self.gridLayout.addWidget(self.labelSeed1, 0, 0, 1, 1)
        self.lineEditSeed1 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSeed1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSeed1.setObjectName(_fromUtf8("lineEditSeed1"))
        self.gridLayout.addWidget(self.lineEditSeed1, 0, 1, 1, 1)
        self.labelSeed2 = QtGui.QLabel(self.layoutWidget)
        self.labelSeed2.setObjectName(_fromUtf8("labelSeed2"))
        self.gridLayout.addWidget(self.labelSeed2, 1, 0, 1, 1)
        self.lineEditSeed2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSeed2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSeed2.setObjectName(_fromUtf8("lineEditSeed2"))
        self.gridLayout.addWidget(self.lineEditSeed2, 1, 1, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 120, 474, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelAddUsername = QtGui.QLabel(self.layoutWidget1)
        self.labelAddUsername.setObjectName(_fromUtf8("labelAddUsername"))
        self.horizontalLayout.addWidget(self.labelAddUsername)
        self.lineEditAddUsername = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditAddUsername.setObjectName(_fromUtf8("lineEditAddUsername"))
        self.horizontalLayout.addWidget(self.lineEditAddUsername)
        self.labelAddHostname = QtGui.QLabel(self.layoutWidget1)
        self.labelAddHostname.setObjectName(_fromUtf8("labelAddHostname"))
        self.horizontalLayout.addWidget(self.labelAddHostname)
        self.lineEditAddHostname = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditAddHostname.setObjectName(_fromUtf8("lineEditAddHostname"))
        self.horizontalLayout.addWidget(self.lineEditAddHostname)
        self.pushButtonAdd = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.labelGenerating = QtGui.QLabel(self.centralwidget)
        self.labelGenerating.setEnabled(True)
        self.labelGenerating.setGeometry(QtCore.QRect(10, 540, 781, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.labelGenerating.setFont(font)
        self.labelGenerating.setObjectName(_fromUtf8("labelGenerating"))
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(420, 200, 361, 42))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelInfo = QtGui.QLabel(self.layoutWidget2)
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        self.verticalLayout.addWidget(self.labelInfo)
        self.lineEditPassword = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEditPassword.setEnabled(True)
        self.lineEditPassword.setReadOnly(True)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.verticalLayout.addWidget(self.lineEditPassword)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionLoad_accounts = QtGui.QAction(mainWindow)
        self.actionLoad_accounts.setObjectName(_fromUtf8("actionLoad_accounts"))
        self.actionSave = QtGui.QAction(mainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(mainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "determ-pwgen by I3ck", None))
        self.tableWidgetAccounts.setSortingEnabled(True)
        self.labelSeed1.setText(_translate("mainWindow", "Enter Seed:", None))
        self.labelSeed2.setText(_translate("mainWindow", "Again:", None))
        self.labelAddUsername.setText(_translate("mainWindow", "Username: ", None))
        self.labelAddHostname.setText(_translate("mainWindow", "@ Hostname:", None))
        self.pushButtonAdd.setText(_translate("mainWindow", "Add", None))
        self.labelGenerating.setText(_translate("mainWindow", "generating password ...", None))
        self.labelInfo.setText(_translate("mainWindow", "TextLabel", None))
        self.actionLoad_accounts.setText(_translate("mainWindow", "import ...", None))
        self.actionSave.setText(_translate("mainWindow", "save", None))
        self.actionSave_as.setText(_translate("mainWindow", "save as ...", None))

