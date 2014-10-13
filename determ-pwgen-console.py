import getpass, json
from inc.DetermPwgen import *

ROUNDS = 1000000


def use_user_input(seed):
	determPwgen = DetermPwgen(seed)

	while True:
		thing = raw_input('\n\nPlease enter the domain or name of the program (e.g. google or outlook): ')
		username = raw_input('Please enter your username for ' + thing + ': ')

		pw = determPwgen.generate_password(thing, username, ROUNDS)

		print "\n" + username + " @ " + thing + ": " + pw


def use_json_file(seed):
	determPwgen = DetermPwgen(seed)

	with open('accounts.json', 'r') as f:
		accounts = json.load(f)

	for account in accounts:
		pw = determPwgen.generate_password(account['hostname'], account['username'], ROUNDS)
		print "\n" + account['username'] + " @ " + account['hostname'] + ": " + pw


def main():
	print "determ-pwgen created by I3ck https://github.com/I3ck/determ-pwgen"
	print "licensed under the MIT License"
	print "version2 (use version1 if you already generated passwords with it)"
	print "using " + str(ROUNDS) + " rounds of sha256\n\n"

	try:
		while True:
			seed = getpass.getpass('password:')
			seed2 = getpass.getpass('again:')
			if seed == seed2:
				break
			print "passwords don't match, please try again"

		while True:
			mode = raw_input('\n\nInput host- and usernames by hand[0]. Use accounts.json[1]: ')
			if mode == "0":
				use_user_input(seed)
				break
			elif mode == "1":
				use_json_file(seed)
				break
			else:
				print "unknown mode, please try again"

	except KeyboardInterrupt:
		print "program exiting"


if __name__ == '__main__':
	main()

