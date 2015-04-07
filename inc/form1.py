# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created: Tue Apr  7 16:01:00 2015
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
        self.tableViewAccounts = QtGui.QTableView(self.centralwidget)
        self.tableViewAccounts.setGeometry(QtCore.QRect(10, 190, 781, 371))
        self.tableViewAccounts.setObjectName(_fromUtf8("tableViewAccounts"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 20, 203, 52))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelSeed1 = QtGui.QLabel(self.widget)
        self.labelSeed1.setObjectName(_fromUtf8("labelSeed1"))
        self.gridLayout.addWidget(self.labelSeed1, 0, 0, 1, 1)
        self.lineEditSeed1 = QtGui.QLineEdit(self.widget)
        self.lineEditSeed1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSeed1.setClearButtonEnabled(False)
        self.lineEditSeed1.setObjectName(_fromUtf8("lineEditSeed1"))
        self.gridLayout.addWidget(self.lineEditSeed1, 0, 1, 1, 1)
        self.labelSeed2 = QtGui.QLabel(self.widget)
        self.labelSeed2.setObjectName(_fromUtf8("labelSeed2"))
        self.gridLayout.addWidget(self.labelSeed2, 1, 0, 1, 1)
        self.lineEditSeed2 = QtGui.QLineEdit(self.widget)
        self.lineEditSeed2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSeed2.setObjectName(_fromUtf8("lineEditSeed2"))
        self.gridLayout.addWidget(self.lineEditSeed2, 1, 1, 1, 1)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(40, 120, 474, 24))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelAddUsername = QtGui.QLabel(self.widget1)
        self.labelAddUsername.setObjectName(_fromUtf8("labelAddUsername"))
        self.horizontalLayout.addWidget(self.labelAddUsername)
        self.lineEditAddUsername = QtGui.QLineEdit(self.widget1)
        self.lineEditAddUsername.setObjectName(_fromUtf8("lineEditAddUsername"))
        self.horizontalLayout.addWidget(self.lineEditAddUsername)
        self.labelAddHostname = QtGui.QLabel(self.widget1)
        self.labelAddHostname.setObjectName(_fromUtf8("labelAddHostname"))
        self.horizontalLayout.addWidget(self.labelAddHostname)
        self.lineEditAddHostname = QtGui.QLineEdit(self.widget1)
        self.lineEditAddHostname.setObjectName(_fromUtf8("lineEditAddHostname"))
        self.horizontalLayout.addWidget(self.lineEditAddHostname)
        self.pushButtonAdd = QtGui.QPushButton(self.widget1)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
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
        self.menuFile.addAction(self.actionLoad_accounts)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "determ-pwgen by I3ck", None))
        self.labelSeed1.setText(_translate("mainWindow", "Enter Seed:", None))
        self.labelSeed2.setText(_translate("mainWindow", "Again:", None))
        self.labelAddUsername.setText(_translate("mainWindow", "Username: ", None))
        self.labelAddHostname.setText(_translate("mainWindow", "@ Hostname:", None))
        self.pushButtonAdd.setText(_translate("mainWindow", "Add", None))
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.actionLoad_accounts.setText(_translate("mainWindow", "import ...", None))
        self.actionSave.setText(_translate("mainWindow", "save", None))
        self.actionSave_as.setText(_translate("mainWindow", "save as ...", None))

