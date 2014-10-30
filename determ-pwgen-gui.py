from Tkinter import *
import json

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
								command=lambda hostname=account['hostname'], username=account['username'] : callback(hostname, username))

		hostnameLabel.place(x=POSITIONS['hostname']['x'], y=y)
		usernameLabel.place(x=POSITIONS['username']['x'], y=y)
		calcButton.place(x=POSITIONS['calc']['x'], y=y)

		y += 50




	pw1Label.place(**POSITIONS['pw1Label'])
	pw2Label.place(**POSITIONS['pw2Label'])

	pw1Entry.place(**POSITIONS['pw1Entry'])
	pw2Entry.place(**POSITIONS['pw2Entry'])




	root.mainloop()

def callback(hostname, username):
	# todo either fill a text field after username @ hostname or open a message box with the values
    print "TODO : " + hostname + " @ " + username


if __name__ == '__main__':
	main()


