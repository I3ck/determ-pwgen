from Tkinter import *


class PasswordDialog:

    def __init__(self, parent, hostname, username, pw):
		top = self.top = Toplevel(parent)
		top.title(username + " @ " + hostname)
		self.infoLabel = Label(top, text=username + " @ " + hostname)
		self.infoLabel.pack()
		self.pwEntry = Entry(top, width=60)
		self.pwEntry.pack()
		self.pwEntry.insert(0, pw)