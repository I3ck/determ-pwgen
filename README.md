determ-pwgen
============

A deterministic password generator for Python3.4

You'll only have to remember one password / seed and can use it to generate a unique password for many websites or programs


Version 5.0.2
=============

Changes version 4 to 5
----------------------
- generating DIFFERENT passwords than version 4 and prior (use version 4 to generate your old passwords and then change them https://github.com/I3ck/determ-pwgen/releases/tag/v4.0.2 )
- generating multiple password types (long, long without special characters, short, short without special characters)
- instead of solely using `sha256` now using a combination of `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`  
- the password generation now uses about 100mb of memory by using a huge random salt for all hashing operations
- the reason for these changes was to not use `sha256` solely because of Bitcoin mining ASICs. An attacker would have to build ASICs solely for `determ-pwgen`. The high memory usage makes this task even harder (see `scrypt`)
- passwords are always mixed-case now  
- passwords with special characters now always include at least one special character



Changes version 3 to 4
----------------------
- Ported to Python3
- In older versions, the hashes might have depended on your system.
I got the same hashes on both Windows and Linux. So it's unlikely that there's a problem, but I suggest checking yourself.
Version 4 and above now always generates the same hashes no matter the system.


Changes version 2 to 3
----------------------
- All passwords are compatible with version 3
- Now using Qt for the gui


Changes version 1 to 2
----------------------
- Generated passwords are now shorter, by using both lower- and uppercase characters (and different from version 1).
- Please use version 1 to recover the old passwords and move to version 2.


The GUI
=======
Enter your seed twice to enable the account table:
![alt tag](https://raw.githubusercontent.com/I3ck/determ-pwgen/master/img/gui-example-1.png)  
After that, simply click onto the `generate` cells to generate a password for the desired account:
![alt tag](https://raw.githubusercontent.com/I3ck/determ-pwgen/master/img/gui-example-2.png)  
Copy and paste your password to where it's needed:
![alt tag](https://raw.githubusercontent.com/I3ck/determ-pwgen/master/img/gui-example-3.png)  
You can also add / remove accounts or generate a password directly, without adding them. `accounts.json` will be updated automatically.
No, I didn't use my seed there ;)

The CLI
=======
```
___________________________________________________________________
| determ-pwgen created by I3ck (Martin Buck)                        |
| https://github.com/I3ck/determ-pwgen                              |
| licensed under the MIT License (see LICENSE file)                 |
| use determ-pwgen-qt.pyw for a graphical user interface            |
|___________________________________________________________________|


Enter your seed:
Seed:
```
Selection of usage mode:
```
Select usage mode:
[1] Input host- and username directly
[2] Use accounts.json
>
```
Mode 1 let's you directly input username and hostname to generate a password:
```
> 1

Enter the username and hostname you want to generate a password for:

Username: user
Hostname: host
--------------------------------------------------------------------------------

user @ host:

Long password:
gspTaZUAIEg9jytoZ1sfaRzd4sAe5qBdZT/PyRFLAmpesMwm4no1DbFHhKDRvFE9QejAtg3IS4+qC7NQIXlVCw==

Long password without special characters:
gspTaZUAIEg9jytoZ1sfaRzd4sAe5qBdZTPyRFLAmpesMwm4no1DbFHhKDRvFE9QejAtg3IS4qC7NQIXlVCw

Short password:
gspTaZUAIEg9jyt)

Short password without special characters:
gspTaZUAIEg9jyto
--------------------------------------------------------------------------------
```

Mode 2 allows you to generate passwords from your accounts.json file:
```
> 2

Edit accounts.json to add or remove accounts
[    0] I3ck@github
[    1] anotherUserOfYou@anotherHostOfYou
Type the number of the account you want to generate the password for
(-1 to abort)
> 0
--------------------------------------------------------------------------------

I3ck @ github:

Long password:
dYW6UQtHK/QcjVmSSiJQ102uIeNdnJMSZozBq0LV0jLoKBH4wjdj1UfkTZG05+vPbKLY1NHa3NVEaHHV
1VsG7w==

Long password without special characters:
dYW6UQtHKQcjVmSSiJQ102uIeNdnJMSZozBq0LV0jLoKBH4wjdj1UfkTZG05vPbKLY1NHa3NVEaHHV1V
sG7w

Short password:
dYW6UQtHK/QcjVmS

Short password without special characters:
dYW6UQtHKQcjVmSS
--------------------------------------------------------------------------------
```
The accounts.json is a simple json file:
```json
[
    {
        "username": "I3ck",
        "hostname": "github"
    },
    {
        "username": "anotherUserOfYou",
        "hostname": "anotherHostOfYou"
    }
]
...
```
which you can edit to add / remove accounts (or use the Qt GUI version)



Usage
=====
To run the console version simply get `Python 3.4` from https://www.python.org/downloads/ and run `python determ-pwgen-console.py`
To run the Qt-gui version you'll have to get `PyQt4` for python3 from http://www.riverbankcomputing.co.uk/software/pyqt/download
and run `python determ-pwgen-qt.pyw`
or double-click the `determ-pwgen-qt.pyw` depending on your OS.


FAQ
===

What are the benefits of using `determ-pwgen`?
--------------------------------------------

### Generally there's two ways people are managing passwords

Either by using the same password for everything
(easy to remember, very insecure)

Using a different password for every service
(difficult to remember, very secure)

### What `determ-pwgen` does differently

Instead of saving all your different passwords (like many password managers do),
`determ-pwgen` can generate any number of passwords, while you only have to remember a single password / seed.

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

```
sha256("This is your input")
	=> 99ae620e26453eb71eaf55be65a337651e0e4f8eff85a8ea60b7196d8db422b9
sha256("this is your input")
	=> 8d031674ce8b92785b8e9dc6fed81745982f98b342d4d65429f9be397d4f1132
```

Also it's impossible to reverse the function. By knowing the output, one can not calculate the input.

### Within `determ-pwgen`

At the beginning the user provides the first part of the input. This is the "password" or "seed" that the user has to remember.


To generate a password, the user now simply provides the hostname and username.
`determ-pwgen` now generates a unique password for every hostname + username combination that the user provides

`determ-pwgen` now does something similar to:
`hash(seed + hostname + username)`


`seed = "asuihdatzwgqe", hostname = "google", and username = "myName"`
`hash("asuihdatzwgqegooglemyName")`



To demonstrate the changes when using another username, once again sha256 is used:
`myName` changed to `myName2`

```
sha256("asuihdatzwgqegooglemyName")
	=> 0cdee0898a8f8ef25c0d18ea72da4d637953903dcaf1dcc5724aafdca07a4e88
sha256("asuihdatzwgqegooglemyName2")
	=> a2e34c47bef2ee7d2a93ba9635f88d5dbbbb0eb1c77084602c926c6782cce3b5
```

That way the user only has to remember the seed and can generate any number of passwords from it
if someone manages to steal the password of "myName", "myName2"'s password would still be save

#Donate
Feeling generous?  
BTC: 19iBhPLkco15ap9HV5UUT5PNoU2djiUiz2
