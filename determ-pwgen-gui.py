from Tkinter import *

def main():
	POSITIONS = {
		'pw1' : {
			'x' : 10,
			'y' : 100
		},
		'pw2' : {
			'x' : 10,
			'y' : 120
		}
	}

	root = Tk()
	root.geometry("500x500")

	pw1 = Entry(root, show="*", width=15)
	pw2 = Entry(root, show="*", width=15)


	pw1.place(**POSITIONS['pw1'])
	pw2.place(**POSITIONS['pw2'])

	root.title("determ-pwgen by I3ck")


	root.mainloop()




if __name__ == '__main__':
	main()