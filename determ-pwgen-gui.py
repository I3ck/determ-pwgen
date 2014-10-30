from Tkinter import *
import tkMessageBox
import json

ROUNDS = 1000000 # todo should be defined at only one place

from inc.DetermPwgen import *

def main():
	POSITIONS = {
		'pw1Label' : {
			'x' : 0,
			'y' : 100
		},
		'pw2Label' : {
			'x' : 0,
			'y' : 120
		},
		'pw1Entry' : {
			'x' : 100,
			'y' : 100
		},
		'pw2Entry' : {
			'x' : 100,
			'y' : 120
		},
		'accounts' : {
			'y' : 200
		},
		'hostname' : {
			'x' : 100
		},
		'username' : {
			'x' : 250
		},
		'calc' : {
			'x' : 300
		}
	}
	SETTINGS = {
		'pw1Label' : {
			'text' : "Enter password: "
		},
		'pw2Label' : {
			'text' : "Again: "
		},
		'pw1Entry' : {
			'width' : 15,
			'show' : "*"
		},
		'pw2Entry' : {
			'width' : 15,
			'show' : "*"
		},
		'calc' : {
			'width' : 10
		}
	}

	root = Tk()
	root.geometry("500x500")
	root.title("determ-pwgen by I3ck")



	pw1Label = Label(root, **SETTINGS['pw1Label'])
	pw2Label = Label(root, **SETTINGS['pw2Label'])

	pw1Entry = Entry(root, **SETTINGS['pw1Entry'])
	pw2Entry = Entry(root, **SETTINGS['pw2Entry'])


	with open('accounts.json', 'r') as f:
		accounts = json.load(f)

	y = POSITIONS['accounts']['y']
	for account in accounts:
		hostnameLabel = Label(root, text=account['hostname'] + " @ ")

		usernameLabel = Label(root, text=account['username'])

		calcButton = Button(	root, text="calc", width=SETTINGS['calc']['width'],
								command=lambda hostname=account['hostname'], username=account['username'] : callback(hostname, username, pw1Entry.get(), pw2Entry.get()))

		hostnameLabel.place(x=POSITIONS['hostname']['x'], y=y)
		usernameLabel.place(x=POSITIONS['username']['x'], y=y)
		calcButton.place(x=POSITIONS['calc']['x'], y=y)

		y += 50




	pw1Label.place(**POSITIONS['pw1Label'])
	pw2Label.place(**POSITIONS['pw2Label'])

	pw1Entry.place(**POSITIONS['pw1Entry'])
	pw2Entry.place(**POSITIONS['pw2Entry'])




	root.mainloop()

def callback(hostname, username, pw1, pw2): #todo rename pw1 and pw2 to seed1 and seed2
	if pw1 != "" and pw1 == pw2:
		determPwgen = DetermPwgen(pw1)
		answer = determPwgen.generate_password(hostname, username, ROUNDS) # todo rename to pw once pw1 was renamed to seed
		tkMessageBox.showinfo("Password for " + username + "@" + hostname , answer) # todo a dialog with copyable text

	else:
		tkMessageBox.showerror("Passwords don't match", "The passwords you provided don't match")



if __name__ == '__main__':
	main()


