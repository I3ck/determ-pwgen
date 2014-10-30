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

	root = Tk()
	root.geometry("500x500")

	pw1Entry = Entry(root, show="*", width=15)
	pw2Entry = Entry(root, show="*", width=15)


	pw1Entry.place(**POSITIONS['pw1Entry'])
	pw2Entry.place(**POSITIONS['pw2Entry'])

	root.title("determ-pwgen by I3ck")


	root.mainloop()




if __name__ == '__main__':
	main()