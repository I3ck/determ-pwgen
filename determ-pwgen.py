import hashlib, getpass, base64

ROUNDS = 1000000

def main():
	print "determ-pwgen by I3ck https://github.com/I3ck/determ-pwgen"
	print "version2 (use version1 if you already generated passwords with it)"
	print "using " + str(ROUNDS) + " rounds of sha256"

	while True:
		seed = getpass.getpass('Please enter your custom seed / password:')
		seed2 = getpass.getpass('Again:')
		if seed == seed2:
			break
		print "passwords / seeds don't match, please try again"

	while True:
		thing = raw_input('Please enter the domain or name of the program (e.g. google or outlook):')
		username = raw_input('Please enter your username for ' + thing + ':')

		pw = seed + thing + username

		for i in range(ROUNDS):
			pw = base64.b64encode((hashlib.sha256(pw).digest()))

		print "your password for " + thing + " with username: " + username + " is:"
		print pw

if __name__ == '__main__':
	main()

