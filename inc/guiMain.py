# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inc/guiMain.ui'
#
# Created: Thu Apr 30 18:11:28 2015
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
        mainWindow.resize(1059, 589)
        mainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 80, 1241, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tableWidgetAccounts = QtGui.QTableWidget(self.centralwidget)
        self.tableWidgetAccounts.setEnabled(True)
        self.tableWidgetAccounts.setGeometry(QtCore.QRect(10, 140, 611, 361))
        self.tableWidgetAccounts.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetAccounts.setObjectName(_fromUtf8("tableWidgetAccounts"))
        self.tableWidgetAccounts.setColumnCount(0)
        self.tableWidgetAccounts.setRowCount(0)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 291, 52))
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
        self.labelGenerating = QtGui.QLabel(self.centralwidget)
        self.labelGenerating.setEnabled(True)
        self.labelGenerating.setGeometry(QtCore.QRect(10, 520, 1041, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.labelGenerating.setFont(font)
        self.labelGenerating.setObjectName(_fromUtf8("labelGenerating"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 100, 590, 28))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
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
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButtonGenerate = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonGenerate.setObjectName(_fromUtf8("pushButtonGenerate"))
        self.horizontalLayout_2.addWidget(self.pushButtonGenerate)
        self.groupBoxPasswords = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxPasswords.setGeometry(QtCore.QRect(630, 130, 421, 301))
        self.groupBoxPasswords.setObjectName(_fromUtf8("groupBoxPasswords"))
        self.pushButtonHide = QtGui.QPushButton(self.groupBoxPasswords)
        self.pushButtonHide.setGeometry(QtCore.QRect(10, 240, 79, 24))
        self.pushButtonHide.setObjectName(_fromUtf8("pushButtonHide"))
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(640, 150, 401, 212))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelInfoLong = QtGui.QLabel(self.layoutWidget2)
        self.labelInfoLong.setObjectName(_fromUtf8("labelInfoLong"))
        self.verticalLayout.addWidget(self.labelInfoLong)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditPasswordLong = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEditPasswordLong.setEnabled(True)
        self.lineEditPasswordLong.setReadOnly(True)
        self.lineEditPasswordLong.setObjectName(_fromUtf8("lineEditPasswordLong"))
        self.horizontalLayout_3.addWidget(self.lineEditPasswordLong)
        self.pushButtonClipboardLong = QtGui.QPushButton(self.layoutWidget2)
        self.pushButtonClipboardLong.setObjectName(_fromUtf8("pushButtonClipboardLong"))
        self.horizontalLayout_3.addWidget(self.pushButtonClipboardLong)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelInfoLongNoSpecial = QtGui.QLabel(self.layoutWidget2)
        self.labelInfoLongNoSpecial.setObjectName(_fromUtf8("labelInfoLongNoSpecial"))
        self.verticalLayout_2.addWidget(self.labelInfoLongNoSpecial)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditPasswordLongNoSpecial = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEditPasswordLongNoSpecial.setEnabled(True)
        self.lineEditPasswordLongNoSpecial.setReadOnly(True)
        self.lineEditPasswordLongNoSpecial.setObjectName(_fromUtf8("lineEditPasswordLongNoSpecial"))
        self.horizontalLayout_4.addWidget(self.lineEditPasswordLongNoSpecial)
        self.pushButtonClipboardLongNoSpecial = QtGui.QPushButton(self.layoutWidget2)
        self.pushButtonClipboardLongNoSpecial.setObjectName(_fromUtf8("pushButtonClipboardLongNoSpecial"))
        self.horizontalLayout_4.addWidget(self.pushButtonClipboardLongNoSpecial)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelInfoShort = QtGui.QLabel(self.layoutWidget2)
        self.labelInfoShort.setObjectName(_fromUtf8("labelInfoShort"))
        self.verticalLayout_3.addWidget(self.labelInfoShort)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEditPasswordShort = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEditPasswordShort.setEnabled(True)
        self.lineEditPasswordShort.setReadOnly(True)
        self.lineEditPasswordShort.setObjectName(_fromUtf8("lineEditPasswordShort"))
        self.horizontalLayout_5.addWidget(self.lineEditPasswordShort)
        self.pushButtonClipboardShort = QtGui.QPushButton(self.layoutWidget2)
        self.pushButtonClipboardShort.setObjectName(_fromUtf8("pushButtonClipboardShort"))
        self.horizontalLayout_5.addWidget(self.pushButtonClipboardShort)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.labelInfoShortNoSpecial = QtGui.QLabel(self.layoutWidget2)
        self.labelInfoShortNoSpecial.setObjectName(_fromUtf8("labelInfoShortNoSpecial"))
        self.verticalLayout_4.addWidget(self.labelInfoShortNoSpecial)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEditPasswordShortNoSpecial = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEditPasswordShortNoSpecial.setEnabled(True)
        self.lineEditPasswordShortNoSpecial.setReadOnly(True)
        self.lineEditPasswordShortNoSpecial.setObjectName(_fromUtf8("lineEditPasswordShortNoSpecial"))
        self.horizontalLayout_6.addWidget(self.lineEditPasswordShortNoSpecial)
        self.pushButtonClipboardShortNoSpecial = QtGui.QPushButton(self.layoutWidget2)
        self.pushButtonClipboardShortNoSpecial.setObjectName(_fromUtf8("pushButtonClipboardShortNoSpecial"))
        self.horizontalLayout_6.addWidget(self.pushButtonClipboardShortNoSpecial)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 19))
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
        mainWindow.setWindowTitle(_translate("mainWindow", "determ-pwgen created by I3ck (Martin Buck)", None))
        self.tableWidgetAccounts.setSortingEnabled(True)
        self.labelSeed1.setText(_translate("mainWindow", "Enter Seed:", None))
        self.labelSeed2.setText(_translate("mainWindow", "Again:", None))
        self.labelGenerating.setText(_translate("mainWindow", "NOTIFY", None))
        self.labelAddUsername.setText(_translate("mainWindow", "Username: ", None))
        self.labelAddHostname.setText(_translate("mainWindow", "@ Hostname:", None))
        self.pushButtonAdd.setText(_translate("mainWindow", "Add", None))
        self.pushButtonGenerate.setText(_translate("mainWindow", "Generate", None))
        self.groupBoxPasswords.setTitle(_translate("mainWindow", "GroupBox", None))
        self.pushButtonHide.setText(_translate("mainWindow", "Hide", None))
        self.labelInfoLong.setText(_translate("mainWindow", "Long password:", None))
        self.pushButtonClipboardLong.setText(_translate("mainWindow", "Copy to Clipboard", None))
        self.labelInfoLongNoSpecial.setText(_translate("mainWindow", "Long password without special characters:", None))
        self.pushButtonClipboardLongNoSpecial.setText(_translate("mainWindow", "Copy to Clipboard", None))
        self.labelInfoShort.setText(_translate("mainWindow", "Short password:", None))
        self.pushButtonClipboardShort.setText(_translate("mainWindow", "Copy to Clipboard", None))
        self.labelInfoShortNoSpecial.setText(_translate("mainWindow", "Short password without special characters:", None))
        self.pushButtonClipboardShortNoSpecial.setText(_translate("mainWindow", "Copy to Clipboard", None))
        self.actionLoad_accounts.setText(_translate("mainWindow", "import ...", None))
        self.actionSave.setText(_translate("mainWindow", "save", None))
        self.actionSave_as.setText(_translate("mainWindow", "save as ...", None))

