from Tkinter import *


class PasswordDialog:

    def __init__(self, parent, hostname, username, pw):
		self.top = Toplevel(parent)
		self.top.title(username + " @ " + hostname)
		self.infoLabel = Label(self.top, text=username + " @ " + hostname)
		self.infoLabel.pack()
		self.pwEntry = Entry(self.top, width=60)
		self.pwEntry.pack()
		self.pwEntry.insert(0, pw)