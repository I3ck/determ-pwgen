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
			'x' : 100,
			'y' : 200
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

	x = POSITIONS['accounts']['x']
	y = POSITIONS['accounts']['y']
	distance = 100
	width = 15
	for account in accounts:
		hostnameLabel = Label(root, text=account['hostname'] + " @ ")


		usernameLabel = Label(root, text=account['username'])

		calcButton = Button(	root, text="calc", width=10,
								command=lambda: callback(account['hostname'], account['username']))

		hostnameLabel.place(x=x, y=y)
		usernameLabel.place(x=x+1.5*distance, y=y)
		calcButton.place(x=x+2.0*distance, y=y)

		y += 50




	pw1Label.place(**POSITIONS['pw1Label'])
	pw2Label.place(**POSITIONS['pw2Label'])

	pw1Entry.place(**POSITIONS['pw1Entry'])
	pw2Entry.place(**POSITIONS['pw2Entry'])




	root.mainloop()

def callback(hostname, username):
    print "TODO : " + hostname + " @ " + username # currently always only prints the last pair, seems like the callback doesnt work


if __name__ == '__main__':
	main()


