determ-pwgen
============

A deterministic password generator

You'll only have to remember one password / seed and can use it to generate a unique password for many websites or programs


Version2
========

Generated passwords are now shorter, by using both lower- and uppercase characters (and different from version 1).
Please use version 1 to recover the old passwords and move to version 2.


FAQ
===

How does this work?
-------------------

determ-pwgem uses a hashing function to generate your passwords  
even the smallest change within the input of a hash function results in a totally different output:  
sha256("This is your input") => 99ae620e26453eb71eaf55be65a337651e0e4f8eff85a8ea60b7196d8db422b9    
sha256("this is your input") => 8d031674ce8b92785b8e9dc6fed81745982f98b342d4d65429f9be397d4f1132  
also it's impossible to reverse the function. By knowing the output, you can't calculate the input  

At the beginning you provide the first part of the input. This is the "password" or "seed" you have to remember  
For every user you now provide the service/hostname and the username for it  
determ-pwgen now generates a unique password for every hostname + username combination that you provide, by doing something similar to:  
hash(seed + hostname + username)  
for   
seed = "asuihdatzwgqe"  
hostname = "google"  
username = "myName"  
hash("asuihdatzwgqegooglemyName")  
would be called  
with sha256:  
sha256("asuihdatzwgqegooglemyName") => 0cdee0898a8f8ef25c0d18ea72da4d637953903dcaf1dcc5724aafdca07a4e88  
if you would now create another user on google with username "myName2" the result would be:  
sha256("asuihdatzwgqegooglemyName2") => a2e34c47bef2ee7d2a93ba9635f88d5dbbbb0eb1c77084602c926c6782cce3b5

That way you only have to remember the seed and can generate any number of passwords from it  
if someone manages to steal the password of "myName", "myName2"'s password would still be save
