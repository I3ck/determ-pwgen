determ-pwgen
============

A deterministic password generator

You'll only have to remember one password / seed and can use it to generate a unique password for many websites or programs  

The GUI
-------
![alt tag](https://raw.githubusercontent.com/I3ck/determ-pwgen/master/img/gui-example-1.png)  
![alt tag](https://raw.githubusercontent.com/I3ck/determ-pwgen/master/img/gui-example-2.png)  
no, I didn't use my seed there ;)  

The cli
-------
```
 ___________________________________________________________________
| determ-pwgen created by I3ck (Martin Buck)                        |
| https://github.com/I3ck/determ-pwgen                              |
| licensed under the MIT License (see LICENSE file)                 |
| use determ-pwgen-qt.pyw for a graphical user interface            |
|___________________________________________________________________|


Enter the following:

password:
```
after entering your password, hostname and username:  
```
 ___________________________________________________________________
| determ-pwgen created by I3ck (Martin Buck)                        |
| https://github.com/I3ck/determ-pwgen                              |
| licensed under the MIT License (see LICENSE file)                 |
| use determ-pwgen-qt.pyw for a graphical user interface            |
|___________________________________________________________________|


Enter the following:

password:
Re-enter password:

Main Menu:

1. Input host and usernames by hand.
2. Use accounts.json
Make a selection: 1


Please enter the domain or name of the program (e.g. google or outlook): github
Please enter your username for github: I3ck

I3ck @ github:
bZEEagyeplME04hqFxxA6vSwSffwL5/1hviZa4H8JwI=


Please enter the domain or name of the program (e.g. google or outlook):
```
no, I didn't use my seed there ;)  




Version 3.3.0
=============


Changes version 2 to 3
----------------------
- All passwords are compatible with version 3  
- Now using Qt for the gui


Changes version 1 to 2
----------------------
- Generated passwords are now shorter, by using both lower- and uppercase characters (and different from version 1).
- Please use version 1 to recover the old passwords and move to version 2.  


Usage
=====
To run the console version simply get `Python 2.7` from https://www.python.org/downloads/ and run `python2 determ-pwgen-console.py`  
To run the Qt-gui version you'll have to get `PyQt4` for python2 from http://www.riverbankcomputing.co.uk/software/pyqt/download  
and run `python2 determ-pwgen-qt.pyw`  
or double-click the `determ-pwgen-qt.pyw` depending on your OS.


FAQ
===

What are the benefits of using determ-pwgen?
--------------------------------------------

### Generally there's two ways people are managing passwords

Either by using the same password for everything  
(easy to remember, very insecure)  

Using a different password for every service  
(difficult to remember, very secure)

### What determ-pwgen does differently

Instead of saving all your different passwords (like many password managers do),  
determ-pwgen can generate any number of passwords, while you only have to remember a single password / seed.  

### Why shouldn't I simply use one of the existing password managers?

Most password managers will save all your passwords in an encrypted database.  
This works perfectly fine, until you want to backup the database onto another device. (in case your hard drive fails)  
Whenever a password is added to your local copy, you have to ensure that all backups are being updated.  
This process is cumbersome, and, if not done correctly, may result in loss of many of your passwords.


How does this work?
-------------------

### The hash function

determ-pwgem uses a hashing function to generate your passwords  
even the smallest change within the input of a hash function results in a totally different output:  

`sha256("This is your input") => 99ae620e26453eb71eaf55be65a337651e0e4f8eff85a8ea60b7196d8db422b9    `  
`sha256("this is your input") => 8d031674ce8b92785b8e9dc6fed81745982f98b342d4d65429f9be397d4f1132  `

Also it's impossible to reverse the function. By knowing the output, one can not calculate the input.

### Usage within determ-pwgen

At the beginning you provide the first part of the input. This is the "password" or "seed" that you have to remember  
This is the **only** thing you have to remember  


To generate a password, the user now simply provides the hostname and username that is used  
determ-pwgen now generates a unique password for every hostname + username combination that the user provides  

determ-pwgen now does something similar to:
`hash(seed + hostname + username)`


`seed = "asuihdatzwgqe", hostname = "google", and username = "myName"`  
`hash("asuihdatzwgqegooglemyName")`



To demonstrate the changes when using another username, once again sha256 is used:  

`sha256("asuihdatzwgqegooglemyName") => 0cdee0898a8f8ef25c0d18ea72da4d637953903dcaf1dcc5724aafdca07a4e88`
`sha256("asuihdatzwgqegooglemyName2") => a2e34c47bef2ee7d2a93ba9635f88d5dbbbb0eb1c77084602c926c6782cce3b5`

That way the user only has to remember the seed and can generate any number of passwords from it  
if someone manages to steal the password of "myName", "myName2"'s password would still be save
