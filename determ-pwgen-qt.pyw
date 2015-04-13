import sys
import json
from PyQt4 import *

from inc.form1 import *
from inc.DetermPwgen import *

ROUNDS = 1000000


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        self.accounts = list()

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonAdd.clicked.connect(self.add)
        self.ui.tableWidgetAccounts.cellClicked.connect(self.generate)

        tableColumns = ["username", "hostname"]
        self.ui.tableWidgetAccounts.setColumnCount(len(tableColumns))
        self.ui.tableWidgetAccounts.setHorizontalHeaderLabels(tableColumns)

        self.load_accounts_file()
        self.update_table()


    def add(self):
        newUser = {
            "username": str(self.ui.lineEditAddUsername.text()),
            "hostname": str(self.ui.lineEditAddHostname.text())
        }

        if newUser["username"] != "" and newUser["hostname"] != "":
            self.accounts.append(newUser)
        
            self.update_table()
            self.save_accounts_file()


    def generate(self, row, column):
        username  = str(self.ui.tableWidgetAccounts.item(row, 0).text())
        hostname = str(self.ui.tableWidgetAccounts.item(row, 1).text())

        seed = str(self.ui.lineEditSeed1.text())  # todo check wheter Seed1 and Seed2 match

        determPwgen = DetermPwgen(seed)
        pw = determPwgen.generate_password(hostname, username, ROUNDS)

        print pw
  

    def save_accounts_file(self):
        with open('accounts.json', 'w') as f:
            json.dump(self.accounts, f, indent=4)


    def load_accounts_file(self):
        with open("accounts.json", "r") as f:
            self.accounts = json.load(f)


    def update_table(self):
        self.ui.tableWidgetAccounts.setRowCount(len(self.accounts))

        for row, account in enumerate(self.accounts):
            widgetUsername = QtGui.QTableWidgetItem(account["username"])
            widgetHostname = QtGui.QTableWidgetItem(account["hostname"])
            widgetGenerate = QtGui.QTableWidgetItem("generate")

            self.ui.tableWidgetAccounts.setItem(row, 0, widgetUsername)
            self.ui.tableWidgetAccounts.setItem(row, 1, widgetHostname)
            self.ui.tableWidgetAccounts.setItem(row, 2, widgetGenerate)
            


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())