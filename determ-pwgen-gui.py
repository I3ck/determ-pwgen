from Tkinter import *

def main():
	POSITIONS = {
		'pw1Entry' : {
			'x' : 10,
			'y' : 100
		},
		'pw2Entry' : {
			'x' : 10,
			'y' : 120
		}
	}
	SETTINGS = {
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

	pw1Entry = Entry(root, **SETTINGS['pw1Entry'])
	pw2Entry = Entry(root, **SETTINGS['pw2Entry'])


	pw1Entry.place(**POSITIONS['pw1Entry'])
	pw2Entry.place(**POSITIONS['pw2Entry'])

	root.title("determ-pwgen by I3ck")


	root.mainloop()




if __name__ == '__main__':
	main()