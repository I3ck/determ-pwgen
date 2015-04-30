"""
    Copyright (c) 2014 - 2015 I3ck (Martin Buck)
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import sys
import json
from PyQt4 import *

from inc.guiMain import *
from inc.DetermPwgen import *
from inc.GenericThread import *
import inc.settings as settings


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.accounts = list()
        self.generatedData = dict()

        self.tableColumns = ["Username", "Hostname", "Generate", "Remove"]

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.init_table()

        self.init_hide_widgets()

        self.init_connections()

        self.load_accounts_file()

        self.update_table()

        self.enable_inputs(False)

        self.notify("Enter your seed first")

# -----------------------------------------------------------------------------

    def init_hide_widgets(self):
        self.hide_notify()

        self.ui.groupBoxPasswords.hide()

        self.ui.lineEditPasswordLong.hide()
        self.ui.labelInfoLong.hide()
        self.ui.pushButtonClipboardLong.hide()

        self.ui.lineEditPasswordLongNoSpecial.hide()
        self.ui.labelInfoLongNoSpecial.hide()
        self.ui.pushButtonClipboardLongNoSpecial.hide()

        self.ui.lineEditPasswordShort.hide()
        self.ui.labelInfoShort.hide()
        self.ui.pushButtonClipboardShort.hide()

        self.ui.lineEditPasswordShortNoSpecial.hide()
        self.ui.labelInfoShortNoSpecial.hide()
        self.ui.pushButtonClipboardShortNoSpecial.hide()

        self.ui.pushButtonHide.hide()

    def init_connections(self):
        self.ui.pushButtonAdd.clicked.connect(self.on_click_add)
        self.ui.pushButtonGenerate.clicked.connect(self.on_click_generate)

        self.ui.pushButtonClipboardLong.clicked.connect(self.on_click_clipboard_long)
        self.ui.pushButtonClipboardLongNoSpecial.clicked.connect(self.on_click_clipboard_long_no_special)
        self.ui.pushButtonClipboardShort.clicked.connect(self.on_click_clipboard_short)
        self.ui.pushButtonClipboardShortNoSpecial.clicked.connect(self.on_click_clipboard_short_no_special)

        self.ui.tableWidgetAccounts.cellClicked.connect(self.on_click_table)

        self.ui.lineEditSeed1.textChanged.connect(self.on_change_seed)
        self.ui.lineEditSeed2.textChanged.connect(self.on_change_seed)

        self.ui.pushButtonHide.clicked.connect(self.hide_generated)

    def init_table(self):
        self.ui.tableWidgetAccounts.setColumnCount(len(self.tableColumns))
        self.ui.tableWidgetAccounts.setHorizontalHeaderLabels(self.tableColumns)

# -----------------------------------------------------------------------------

    def on_click_add(self):
        newuser = {
            "username": str(self.ui.lineEditAddUsername.text()),
            "hostname": str(self.ui.lineEditAddHostname.text())
        }

        if newuser["username"] != "" and newuser["hostname"] != "":
            self.accounts.append(newuser)

            self.update_table()
            self.save_accounts_file()

    def on_click_generate(self):
        username = str(self.ui.lineEditAddUsername.text())
        hostname = str(self.ui.lineEditAddHostname.text())

        if username != "" and hostname != "":
            seed1 = str(self.ui.lineEditSeed1.text())
            seed2 = str(self.ui.lineEditSeed2.text())

            if seed1 == "":
                self.notify("Seed can't be empty. Please enter your seed / password")

            elif seed1 != seed2:
                self.notify("Seeds don't match, please re-type them")

            else:
                self.notify("generating password for " + username + "@" + hostname + "...")

                self.hide_generated()

                self.generic_thread = GenericThread(self.threaded_generate, seed1, hostname, username)
                self.connect(self.generic_thread, self.generic_thread.signal, self.threaded_generate_done)
                self.generic_thread.start()

        else:
            self.notify("Please enter a username and hostname")

    def on_click_table(self, row, column):
        if self.tableColumns[column] == "Generate":
            self.generate_password(row)

        elif self.tableColumns[column] == "Remove":
            self.remove_account(row)

        else:
            self.notify("Either click Remove or Generate")

    def on_click_clipboard_long(self):
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.ui.lineEditPasswordLong.text(), mode=cb.Clipboard)
        self.notify("Copied long password to clipboard")

    def on_click_clipboard_long_no_special(self):
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.ui.lineEditPasswordLongNoSpecial.text(), mode=cb.Clipboard)
        self.notify("Copied long password without special characters to clipboard")

    def on_click_clipboard_short(self):
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.ui.lineEditPasswordShort.text(), mode=cb.Clipboard)
        self.notify("Copied short password to clipboard")

    def on_click_clipboard_short_no_special(self):
        cb = QtGui.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.ui.lineEditPasswordShortNoSpecial.text(), mode=cb.Clipboard)
        self.notify("Copied short password without special characters to clipboard")

# -----------------------------------------------------------------------------

    def on_change_seed(self):
        seed1 = str(self.ui.lineEditSeed1.text())
        seed2 = str(self.ui.lineEditSeed2.text())
        enable = False
        self.hide_notify()

        if seed1 != "" and seed2 != "":
            if seed1 != seed2:
                self.notify("Seeds don't match")
            else:
                enable = True

        self.enable_inputs(enable)

# -----------------------------------------------------------------------------

    def update_table(self):
        self.ui.tableWidgetAccounts.setRowCount(len(self.accounts))

        for row, account in enumerate(self.accounts):
            widget_username = QtGui.QTableWidgetItem(account["username"])
            widget_hostname = QtGui.QTableWidgetItem(account["hostname"])
            widget_generate = QtGui.QTableWidgetItem("click")
            widget_remove = QtGui.QTableWidgetItem("click")

            widget_generate.setTextAlignment(QtCore.Qt.AlignCenter)
            widget_remove.setTextAlignment(QtCore.Qt.AlignCenter)

            self.ui.tableWidgetAccounts.setItem(row, 0, widget_username)
            self.ui.tableWidgetAccounts.setItem(row, 1, widget_hostname)
            self.ui.tableWidgetAccounts.setItem(row, 2, widget_generate)
            self.ui.tableWidgetAccounts.setItem(row, 3, widget_remove)

# -----------------------------------------------------------------------------

    def enable_inputs(self, enable=True):
        self.ui.tableWidgetAccounts.setEnabled(enable)

        self.ui.lineEditAddUsername.setEnabled(enable)
        self.ui.lineEditAddHostname.setEnabled(enable)

        self.ui.pushButtonAdd.setEnabled(enable)
        self.ui.pushButtonGenerate.setEnabled(enable)

# -----------------------------------------------------------------------------

    def notify(self, text):
        self.ui.labelGenerating.show()
        self.ui.labelGenerating.setText(text)

# -----------------------------------------------------------------------------

    def hide_notify(self):
        self.ui.labelGenerating.hide()

    def hide_generated(self):
        self.ui.groupBoxPasswords.hide()

        self.ui.labelInfoLong.hide()
        self.ui.lineEditPasswordLong.hide()
        self.ui.pushButtonClipboardLong.hide()

        self.ui.labelInfoLongNoSpecial.hide()
        self.ui.lineEditPasswordLongNoSpecial.hide()
        self.ui.pushButtonClipboardLongNoSpecial.hide()

        self.ui.labelInfoShort.hide()
        self.ui.lineEditPasswordShort.hide()
        self.ui.pushButtonClipboardShort.hide()

        self.ui.labelInfoShortNoSpecial.hide()
        self.ui.lineEditPasswordShortNoSpecial.hide()
        self.ui.pushButtonClipboardShortNoSpecial.hide()

        self.ui.pushButtonHide.hide()

# -----------------------------------------------------------------------------

    def remove_account(self, row):
        username = str(self.ui.tableWidgetAccounts.item(row, 0).text())
        hostname = str(self.ui.tableWidgetAccounts.item(row, 1).text())
        reply = QtGui.QMessageBox.question(self,
                                           "Are you sure?",
                                           "Are you sure you want to remove " + username + "@" + hostname,
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            del(self.accounts[row])
            self.save_accounts_file()
            self.update_table()

# -----------------------------------------------------------------------------

    def generate_password(self, row):
        seed1 = str(self.ui.lineEditSeed1.text())
        seed2 = str(self.ui.lineEditSeed2.text())

        if seed1 == "":
            self.notify("Seed can't be empty. Please enter your seed / password")

        elif seed1 != seed2:
            self.notify("Seeds don't match, please re-type them")

        else:
            username = str(self.ui.tableWidgetAccounts.item(row, 0).text())
            hostname = str(self.ui.tableWidgetAccounts.item(row, 1).text())

            self.notify("Generating password for " + username + "@" + hostname + "...")

            self.hide_generated()

            self.generic_thread = GenericThread(self.threaded_generate, seed1, hostname, username)
            self.connect(self.generic_thread, self.generic_thread.signal, self.threaded_generate_done)
            self.generic_thread.start()

# -----------------------------------------------------------------------------

    def threaded_generate(self, seed, hostname, username):
        determ_pwgen = DetermPwgen(seed)

        pw = determ_pwgen.generate_password(hostname, username, settings.HASHING_ROUNDS)

        self.generatedData["hostname"] = hostname
        self.generatedData["username"] = username
        self.generatedData["pw"] = pw

    def threaded_generate_done(self):
        hostname = self.generatedData["hostname"]
        username = self.generatedData["username"]
        pw = self.generatedData["pw"]

        self.hide_notify()

        self.ui.groupBoxPasswords.show()

        self.ui.labelInfoLong.show()
        self.ui.lineEditPasswordLong.show()
        self.ui.pushButtonClipboardLong.show()

        self.ui.labelInfoLongNoSpecial.show()
        self.ui.lineEditPasswordLongNoSpecial.show()
        self.ui.pushButtonClipboardLongNoSpecial.show()

        self.ui.labelInfoShort.show()
        self.ui.lineEditPasswordShort.show()
        self.ui.pushButtonClipboardShort.show()

        self.ui.labelInfoShortNoSpecial.show()
        self.ui.lineEditPasswordShortNoSpecial.show()
        self.ui.pushButtonClipboardShortNoSpecial.show()

        self.ui.groupBoxPasswords.setTitle("Passwords for " + username + "@" + hostname)

        self.ui.lineEditPasswordLong.setText(pw.PWLONG)
        self.ui.lineEditPasswordLongNoSpecial.setText(pw.PWLONG_NO_SPECIAL)
        self.ui.lineEditPasswordShort.setText(pw.PWSHORT)
        self.ui.lineEditPasswordShortNoSpecial.setText(pw.PWSHORT_NO_SPECIAL)

        self.ui.pushButtonHide.show()

# -----------------------------------------------------------------------------

    def save_accounts_file(self):
        with open(settings.PATH_ACCOUNTS_FILE, 'w') as f:
            json.dump(self.accounts, f, indent=4)
        self.notify("Changes written to " + settings.PATH_ACCOUNTS_FILE)

    def load_accounts_file(self):
        with open(settings.PATH_ACCOUNTS_FILE, "r") as f:
            self.accounts = json.load(f)

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
