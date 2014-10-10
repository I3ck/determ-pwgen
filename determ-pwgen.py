import hashlib, getpass

ROUNDS = 1000000

def main():
	print "using " + str(ROUNDS) + " rounds of sha256"
	print "make sure to remember these settings in case you lose the program"

	seed = getpass.getpass('Please enter your custom seed / password:')

	while True:
		thing = raw_input('Please enter the domain or name of the program (e.g. google or outlook):')
		username = raw_input('Please enter your username for ' + thing + ':')

		pw = seed + thing + username

		for i in range(ROUNDS):
			pw = hashlib.sha256(pw).hexdigest()

		print "your password for " + thing + " with username: " + username + " is:"
		print pw

if __name__ == '__main__':
	main()
