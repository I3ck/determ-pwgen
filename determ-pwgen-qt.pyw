import sys
import json
from PyQt4 import *

from inc.form1 import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        self.accounts = list()

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonAdd.clicked.connect(self.add)

        COLUMNS = 3
        self.ui.tableWidgetAccounts.setColumnCount(COLUMNS)
        self.ui.tableWidgetAccounts.setHorizontalHeaderLabels(["username", "hostname", "generate"])

        self.load_accounts_file()
        self.update_table()


    def add(self):
        username = self.ui.lineEditAddUsername.text()
        hostname = self.ui.lineEditAddHostname.text()
        print "username: ", username
        print "hostname: ", hostname
        print "TODO add"


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
