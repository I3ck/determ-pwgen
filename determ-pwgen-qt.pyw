import sys
import json
from PyQt4 import *

from inc.form1 import *
from inc.DetermPwgen import *

ROUNDS = 1000000


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.accounts = list()

        self.tableColumns = ["Username", "Hostname", "generate", "delete"]

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.init_table()

        self.init_hide_widgets()

        self.init_connections()

        self.load_accounts_file()

        self.update_table()


    def init_hide_widgets(self):
        self.hide_notify()
        self.ui.lineEditPassword.hide()
        self.ui.labelInfo.hide()


    def init_connections(self):
        self.ui.pushButtonAdd.clicked.connect(self.add)

        self.ui.tableWidgetAccounts.cellClicked.connect(self.click_table)


    def init_table(self):
        self.ui.tableWidgetAccounts.setColumnCount(len(self.tableColumns))
        self.ui.tableWidgetAccounts.setHorizontalHeaderLabels(self.tableColumns)


    def add(self):
        newUser = {
            "username": str(self.ui.lineEditAddUsername.text()),
            "hostname": str(self.ui.lineEditAddHostname.text())
        }

        if newUser["username"] != "" and newUser["hostname"] != "":
            self.accounts.append(newUser)

            self.update_table()
            self.save_accounts_file()


    def notify(self, text):
        self.ui.labelGenerating.show()
        self.ui.labelGenerating.setText(text)


    def hide_notify(self):
        self.ui.labelGenerating.hide()

    def click_table(self, row, column):
        if self.tableColumns[column] == "generate":
            self.generate(row)

        elif self.tableColumns[column] == "delete":
            self.delete(row)

        else:
            self.notify("Either click delete or generate")


    def delete(self, row):
        username  = str(self.ui.tableWidgetAccounts.item(row, 0).text())
        hostname = str(self.ui.tableWidgetAccounts.item(row, 1).text())
        reply = QtGui.QMessageBox.question(self,
            "Are you sure?",
            "Are you sure you want to delete " + username + "@" + hostname,
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            del(self.accounts[row])
            self.save_accounts_file()
            self.update_table()


    def generate(self, row):
        seed1 = str(self.ui.lineEditSeed1.text())
        seed2 = str(self.ui.lineEditSeed2.text())

        if seed1 == "":
            self.notify("Seed can't be empty. Please enter your seed / password")

        elif seed1 != seed2:
            self.notify("Seeds don't match, please re-type them")

        else:
            username  = str(self.ui.tableWidgetAccounts.item(row, 0).text())
            hostname = str(self.ui.tableWidgetAccounts.item(row, 1).text())

            self.notify("generating password for " + username + "@" + hostname + "...")

            self.genericThread = GenericThread(self.generate_bg, seed1, hostname, username)
            self.genericThread.start()


    def generate_bg(self,seed, hostname, username):
        determPwgen = DetermPwgen(seed)

        pw = determPwgen.generate_password(hostname, username, ROUNDS)

        self.hide_notify()

        self.ui.labelInfo.show()
        self.ui.lineEditPassword.show()

        self.ui.labelInfo.setText("password for " + username + "@" + hostname + ":")
        self.ui.lineEditPassword.setText(pw)


    def save_accounts_file(self):
        with open('accounts.json', 'w') as f:
            json.dump(self.accounts, f, indent=4)
        self.notify("Changes written to accounts.json")


    def load_accounts_file(self):
        with open("accounts.json", "r") as f:
            self.accounts = json.load(f)


    def update_table(self):
        self.ui.tableWidgetAccounts.setRowCount(len(self.accounts))

        for row, account in enumerate(self.accounts):
            widgetUsername = QtGui.QTableWidgetItem(account["username"])
            widgetHostname = QtGui.QTableWidgetItem(account["hostname"])
            widgetGenerate = QtGui.QTableWidgetItem("click")
            widgetDelete = QtGui.QTableWidgetItem("click")

            self.ui.tableWidgetAccounts.setItem(row, 0, widgetUsername)
            self.ui.tableWidgetAccounts.setItem(row, 1, widgetHostname)
            self.ui.tableWidgetAccounts.setItem(row, 2, widgetGenerate)
            self.ui.tableWidgetAccounts.setItem(row, 3, widgetDelete)


class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args,**self.kwargs)
        return


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
