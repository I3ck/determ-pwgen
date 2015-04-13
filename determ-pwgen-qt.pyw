import sys
from PyQt4 import *

from inc.form1 import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonAdd.clicked.connect(self.add)

    def add(self):
        username = self.ui.lineEditAddUsername.text()
        hostname = self.ui.lineEditAddHostname.text()
        print "username: ", username
        print "hostname: ", hostname
        print "TODO add"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
