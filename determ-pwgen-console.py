"""
    Copyright (c) 2014 - 2015 I3ck (Martin Buck)
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import getpass, json
from inc.DetermPwgen import *
import inc.settings as settings

def welcome_banner():
	print("\n")
	print " ___________________________________________________________________ "
	print "| determ-pwgen created by I3ck (Martin Buck)                        |"
	print "| https://github.com/I3ck/determ-pwgen                              |"
	print "| licensed under the MIT License (see LICENSE file)                 |"
	print "| use determ-pwgen-qt.pyw for a graphical user interface            |"
	print "|___________________________________________________________________|"
	print("\n")


def get_print_string(hostname, username, pw):
	return username + " @ " + hostname + ":\n" + pw


def use_user_input(seed):
	determPwgen = DetermPwgen(seed)

	while True:
		hostname = raw_input('\n\nPlease enter the domain or name of the program (e.g. google or outlook): ')
		username = raw_input('Please enter your username for ' + hostname + ': ')

		pw = determPwgen.generate_password(hostname, username, settings.ROUNDS)

		print "\n" + get_print_string(hostname, username, pw)


def use_json_file(seed):
	determPwgen = DetermPwgen(seed)

	with open(settings.PATH_ACCOUNTS_FILE, 'r') as f:
		accounts = json.load(f)

	for account in accounts:
		pw = determPwgen.generate_password(account['hostname'], account['username'], settings.ROUNDS)
		print "\n" + get_print_string(account['hostname'], account['username'], pw)


def main():
	welcome_banner()

	try:
		while True:
			print("Enter the following: \n")
			seed = getpass.getpass('password: ')
			seed2 = getpass.getpass('Re-enter password: ')
			if seed == seed2:
				break
			print "passwords don't match, please try again"

		while True:
			print("\nMain Menu: ")
			mode = raw_input('\n1. Input host and usernames by hand.\n2. Use ' + settings.PATH_ACCOUNTS_FILE + '\nMake a selection: ')
			if mode == "1":
				use_user_input(seed)
				break
			elif mode == "2":
				use_json_file(seed)
				use_user_input(seed)
				break
			else:
				print "unknown mode, please try again"

	except KeyboardInterrupt:
		print "program exiting"


if __name__ == '__main__':
	main()

