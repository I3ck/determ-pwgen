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


import getpass
import json
from inc.DetermPwgen import *
import inc.settings as settings


PROMPT = "> "


def print_welcome_banner():
    print ""
    print " ___________________________________________________________________ "
    print "| determ-pwgen created by I3ck (Martin Buck)                        |"
    print "| https://github.com/I3ck/determ-pwgen                              |"
    print "| licensed under the MIT License (see LICENSE file)                 |"
    print "| use determ-pwgen-qt.pyw for a graphical user interface            |"
    print "|___________________________________________________________________|"
    print ""


def print_result(hostname, username, pw):
    print "--------------------------------------------------------------------------------"
    print username + " @ " + hostname + ":\n" + pw
    print "--------------------------------------------------------------------------------"


def use_user_input(seed):
    determ_pwgen = DetermPwgen(seed)

    print "\n\nEnter the username and hostname you want to generate a password for:"

    while True:
        username = raw_input("\nUsername: ")
        hostname = raw_input("Hostname: ")

        pw = determ_pwgen.generate_password(hostname, username, settings.ROUNDS)

        print_result(hostname, username, pw)


def use_json_file(seed):
    determ_pwgen = DetermPwgen(seed)

    with open(settings.PATH_ACCOUNTS_FILE, 'r') as f:
        accounts = json.load(f)

    print ""
    print "Edit " + settings.PATH_ACCOUNTS_FILE + " to add or remove accounts"
    for i, account in enumerate(accounts):
        print "[" + str(i).rjust(5) + "]" + " " + account["username"] + "@" + account["hostname"]

    print "Type the number of the account you want to generate the password for"
    print "(-1 to abort)"
    while True:
        index = int(raw_input(PROMPT))
        if index == -1:
            break
        if 0 <= index < len(accounts):
            account = accounts[index]
            pw = determ_pwgen.generate_password(account["hostname"], account["username"], settings.ROUNDS)
            print_result(account["hostname"], account["username"], pw)


def main():
    print_welcome_banner()

    try:
        while True:
            print "\nEnter your seed:"
            seed = getpass.getpass('Seed: ')
            seed2 = getpass.getpass('Again: ')
            if seed == seed2:
                break
            print "Seeds don't match, please try again."

        while True:
            print "\nSelect usage mode:"
            print "[1] Input host- and username directly"
            print "[2] Use " + settings.PATH_ACCOUNTS_FILE
            mode = raw_input(PROMPT)
            if mode == "1":
                use_user_input(seed)
                break
            elif mode == "2":
                use_json_file(seed)
                use_user_input(seed)
                break
            else:
                print "Unknown mode, please try again"

    except KeyboardInterrupt:
        print "\ndeterm-pwgen exiting"


if __name__ == '__main__':
    main()

