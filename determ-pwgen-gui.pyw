from Tkinter import *
import tkMessageBox
import json

from inc.DetermPwgen import *
from inc.PasswordDialog import *

ROUNDS = 1000000

POSITIONS = {
	'seed1Label' : {
		'x' : 25,
		'y' : 25
	},
	'seed2Label' : {
		'x' : 25,
		'y' : 45
	},
	'seed1Entry' : {
		'x' : 125,
		'y' : 25
	},
	'seed2Entry' : {
		'x' : 125,
		'y' : 45
	},
	'hostnameLabel' : {
		'x' : 275,
		'y' : 100
	},
	'usernameLabel' : {
		'x' : 100,
		'y' : 100
	},
	'hostnameEntry' : {
		'x' : 350,
		'y' : 100
	},
	'usernameEntry' : {
		'x' : 175,
		'y' : 100
	},
	'accounts' : {
		'y' : 150,
		'distance' : 50
	},
	'info' : {
		'x' : 100
	},
	'calc' : {
		'x' : 25
	},
	'add' : {
		'x' : 450
	}
}

SETTINGS = {
	'seed1Label' : {
		'text' : "enter seed: "
	},
	'seed2Label' : {
		'text' : "again: "
	},
	'seed1Entry' : {
		'width' : 15,
		'show' : "*"
	},
	'seed2Entry' : {
		'width' : 15,
		'show' : "*"
	},
	'hostnameLabel' : {
		'text' : "hostname"
	},
	'usernameLabel' : {
		'text' : "username"
	},
	'hostnameEntry' : {
		'width' : 15
	},
	'usernameEntry' : {
		'width' : 15
	},
	'calc' : {
		'width' : 10
	},
	'add' : {
		'width' : 10
	}
}

class MainWindow:

	def __init__(self):
		self.root = Tk()
		self.root.geometry("600x800")
		self.root.title("determ-pwgen by I3ck")

		seed1Label = Label(self.root, **SETTINGS['seed1Label'])
		seed2Label = Label(self.root, **SETTINGS['seed2Label'])

		seed1Entry = Entry(self.root, **SETTINGS['seed1Entry'])
		seed2Entry = Entry(self.root, **SETTINGS['seed2Entry'])

		hostnameLabel = Label(self.root, **SETTINGS['hostnameLabel'])
		usernameLabel = Label(self.root, **SETTINGS['usernameLabel'])

		hostnameEntry = Entry(self.root, **SETTINGS['hostnameEntry'])
		usernameEntry = Entry(self.root, **SETTINGS['usernameEntry'])

		calcButton = Button(	self.root, text="get pw", width=SETTINGS['calc']['width'],
								command=lambda  : self.showPassword(hostnameEntry.get(), usernameEntry.get(), seed1Entry.get(), seed2Entry.get()))

		calcButton.place(x=POSITIONS['calc']['x'], y=POSITIONS['usernameLabel']['y'])




		with open('accounts.json', 'r') as f:
			accounts = json.load(f)


		self.y = POSITIONS['accounts']['y']
		for account in accounts:
			infoLabel = Label(self.root, text=account['username'] + " @ " + account['hostname'])

			calcButton = Button(	self.root, text="get pw", width=SETTINGS['calc']['width'],
									command=lambda hostname=account['hostname'], username=account['username'] : self.showPassword(hostname, username, seed1Entry.get(), seed2Entry.get()))

			infoLabel.place(x=POSITIONS['info']['x'], y=self.y)
			calcButton.place(x=POSITIONS['calc']['x'], y=self.y)

			self.y += POSITIONS['accounts']['distance']

		addButton = Button(	self.root, text="add", width=SETTINGS['add']['width'],
							command=lambda : self.addAccount(hostnameEntry.get(), usernameEntry.get()))

		seed1Label.place(**POSITIONS['seed1Label'])
		seed2Label.place(**POSITIONS['seed2Label'])

		seed1Entry.place(**POSITIONS['seed1Entry'])
		seed2Entry.place(**POSITIONS['seed2Entry'])

		hostnameLabel.place(**POSITIONS['hostnameLabel'])
		usernameLabel.place(**POSITIONS['usernameLabel'])

		hostnameEntry.place(**POSITIONS['hostnameEntry'])
		usernameEntry.place(**POSITIONS['usernameEntry'])

		addButton.place(x=POSITIONS['add']['x'], y=POSITIONS['usernameLabel']['y'])

		self.root.mainloop()

	def showPassword(self,hostname, username, seed1, seed2):
		if seed1 == "":
			tkMessageBox.showerror("Invalid seed", "You have to provide a seed first")

		elif seed1 != seed2:
			tkMessageBox.showerror("Invalid seed", "The seeds you provided don't match")

		else:
			determPwgen = DetermPwgen(seed1)
			pw = determPwgen.generate_password(hostname, username, ROUNDS)
			passwordDialog = PasswordDialog(self.root, hostname, username, pw)
			self.root.wait_window(passwordDialog.top)

	def addAccount(self,hostname, username):

		with open('accounts.json', 'r') as f:
			accounts = json.load(f)

		new_account = {
			'hostname' : hostname,
			'username' : username
		}
		accounts.append(new_account)

		with open('accounts.json', 'w') as f:
			json.dump(accounts, f)

		infoLabel = Label(self.root, text=username + " @ " + hostname)

		calcButton = Button(	self.root, text="get pw", width=SETTINGS['calc']['width'],
								command=lambda hostname=hostname, username=username : showPassword(hostname, username, seed1Entry.get(), seed2Entry.get()))

		infoLabel.place(x=POSITIONS['info']['x'], y=self.y)
		calcButton.place(x=POSITIONS['calc']['x'], y=self.y)

		self.y += POSITIONS['accounts']['distance']

if __name__ == '__main__':
	mainWindow = MainWindow()
