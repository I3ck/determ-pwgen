import getpass
from inc.DetermPwgen import *

ROUNDS = 1000000

def main():
	print "determ-pwgen created by I3ck https://github.com/I3ck/determ-pwgen"
	print "licensed under the MIT License"
	print "version2 (use version1 if you already generated passwords with it)"
	print "using " + str(ROUNDS) + " rounds of sha256"


	try:
		while True:
			seed = getpass.getpass('password:')
			seed2 = getpass.getpass('again:')
			if seed == seed2:
				break
			print "passwords don't match, please try again"

		determPwgen = DetermPwgen(seed)

		while True:
			thing = raw_input('\n\nPlease enter the domain or name of the program (e.g. google or outlook): ')
			username = raw_input('Please enter your username for ' + thing + ': ')

			pw = determPwgen.generate_password(thing, username, ROUNDS)

			print "\n" + username + " @ " + thing + ": " + pw

	except KeyboardInterrupt:
		print "program exiting"

if __name__ == '__main__':
	main()

