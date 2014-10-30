from Tkinter import *

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



	pw1Label.place(**POSITIONS['pw1Label'])
	pw2Label.place(**POSITIONS['pw2Label'])

	pw1Entry.place(**POSITIONS['pw1Entry'])
	pw2Entry.place(**POSITIONS['pw2Entry'])




	root.mainloop()




if __name__ == '__main__':
	main()