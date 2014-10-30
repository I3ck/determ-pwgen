from Tkinter import *
import tkMessageBox
import json

# todo it should be possible to directly edit the .json from the gui

ROUNDS = 1000000 # todo should be defined at only one place

from inc.DetermPwgen import *

def main():
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
		'accounts' : {
			'y' : 100
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
		'calc' : {
			'width' : 10
		}
	}

	root = Tk()
	root.geometry("400x600")
	root.title("determ-pwgen by I3ck")

	# todo add info box similar to console version



	seed1Label = Label(root, **SETTINGS['seed1Label'])
	seed2Label = Label(root, **SETTINGS['seed2Label'])

	seed1Entry = Entry(root, **SETTINGS['seed1Entry'])
	seed2Entry = Entry(root, **SETTINGS['seed2Entry'])


	with open('accounts.json', 'r') as f:
		accounts = json.load(f)

	y = POSITIONS['accounts']['y']
	for account in accounts:
		infoLabel = Label(root, text=account['hostname'] + " @ " + account['username'])

		calcButton = Button(	root, text="get pw", width=SETTINGS['calc']['width'],
								command=lambda hostname=account['hostname'], username=account['username'] : callback(hostname, username, seed1Entry.get(), seed2Entry.get()))

		infoLabel.place(x=POSITIONS['info']['x'], y=y)
		calcButton.place(x=POSITIONS['calc']['x'], y=y)

		y += 50




	seed1Label.place(**POSITIONS['seed1Label'])
	seed2Label.place(**POSITIONS['seed2Label'])

	seed1Entry.place(**POSITIONS['seed1Entry'])
	seed2Entry.place(**POSITIONS['seed2Entry'])




	root.mainloop()

def callback(hostname, username, seed1, seed2): #todo rename seed1 and seed2 to seed1 and seed2
	if seed1 != "" and seed1 == seed2:
		determPwgen = DetermPwgen(seed1)
		pw = determPwgen.generate_password(hostname, username, ROUNDS)
		tkMessageBox.showinfo("Password for " + username + "@" + hostname , pw) # todo a dialog with copyable text

	else:
		tkMessageBox.showerror("Seeds don't match", "The seeds you provided don't match")



if __name__ == '__main__':
	main()


