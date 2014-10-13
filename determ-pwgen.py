import hashlib, getpass, base64

ROUNDS = 1000000

class DetermPwgen:

	def __init__(self, seed):
		self._seed = seed

	def generate_password(self, hostname, username, rounds):
		pw = self._seed + hostname + username

		for i in range(rounds):
			pw = base64.b64encode((hashlib.sha256(pw).digest()))

		return pw





def main():
	print "determ-pwgen created by I3ck https://github.com/I3ck/determ-pwgen"
	print "licensed under the MIT License"
	print "version2 (use version1 if you already generated passwords with it)"
	print "using " + str(ROUNDS) + " rounds of sha256"

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

if __name__ == '__main__':
	main()

