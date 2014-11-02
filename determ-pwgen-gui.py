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
	}
}


def main():

	root = Tk()
	root.geometry("500x800")
	root.title("determ-pwgen by I3ck")

	seed1Label = Label(root, **SETTINGS['seed1Label'])
	seed2Label = Label(root, **SETTINGS['seed2Label'])

	seed1Entry = Entry(root, **SETTINGS['seed1Entry'])
	seed2Entry = Entry(root, **SETTINGS['seed2Entry'])

	hostnameLabel = Label(root, **SETTINGS['hostnameLabel'])
	usernameLabel = Label(root, **SETTINGS['usernameLabel'])

	hostnameEntry = Entry(root, **SETTINGS['hostnameEntry'])
	usernameEntry = Entry(root, **SETTINGS['usernameEntry'])

	calcButton = Button(	root, text="get pw", width=SETTINGS['calc']['width'],
							command=lambda  : callback(root, hostnameEntry.get(), usernameEntry.get(), seed1Entry.get(), seed2Entry.get()))

	calcButton.place(x=POSITIONS['calc']['x'], y=POSITIONS['usernameLabel']['y'])


	with open('accounts.json', 'r') as f:
		accounts = json.load(f)


	y = POSITIONS['accounts']['y']
	for account in accounts:
		infoLabel = Label(root, text=account['hostname'] + " @ " + account['username'])

		calcButton = Button(	root, text="get pw", width=SETTINGS['calc']['width'],
								command=lambda hostname=account['hostname'], username=account['username'] : callback(root,hostname, username, seed1Entry.get(), seed2Entry.get()))

		infoLabel.place(x=POSITIONS['info']['x'], y=y)
		calcButton.place(x=POSITIONS['calc']['x'], y=y)

		y += POSITIONS['accounts']['distance']


	seed1Label.place(**POSITIONS['seed1Label'])
	seed2Label.place(**POSITIONS['seed2Label'])

	seed1Entry.place(**POSITIONS['seed1Entry'])
	seed2Entry.place(**POSITIONS['seed2Entry'])

	hostnameLabel.place(**POSITIONS['hostnameLabel'])
	usernameLabel.place(**POSITIONS['usernameLabel'])

	hostnameEntry.place(**POSITIONS['hostnameEntry'])
	usernameEntry.place(**POSITIONS['usernameEntry'])


	root.mainloop()


def callback(root,hostname, username, seed1, seed2):
	if seed1 == "":
		tkMessageBox.showerror("Invalid seed", "You have to provide a seed first")

	elif seed1 != seed2:
		tkMessageBox.showerror("Invalid seed", "The seeds you provided don't match")

	else:
		determPwgen = DetermPwgen(seed1)
		pw = determPwgen.generate_password(hostname, username, ROUNDS)
		passwordDialog = PasswordDialog(root, hostname, username, pw)
		root.wait_window(passwordDialog.top)


if __name__ == '__main__':
	main()
