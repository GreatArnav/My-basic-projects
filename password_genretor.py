#! /usr/bin/env python3

from random import randint, choice, shuffle
import string

print("Welcome to Arnav's password genretor")


# variable


num = int(input('enter the number of number in the pasword-'))
upper = int(input('enter the number of upper case(capital letter) in password-'))
lower = int(input('enter the number of lower case(small letter) in pasword-'))
small = 'abcdefghijklmnopqrstuvwxyz'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = input("enter the special character[if you don't than enter 'n' to escape]-")
password = ""
# loop

for num2 in range(num):
	r = randint(0,9)
	r = str(r)
	password = password+r
for upper2 in range(upper):
	r = choice(capital)
	password = password+r
for lower2 in range(lower):
	r = choice(small)
	password = password+r

password = list(password)
shuffle(password)

password = ''.join(password)

if special == 'n':
	pass
else:
	pasword = password+special

print("your password is ready\n",password)

save = input("If you want save password in file\nEnter the 'Y'\n if not enter 'n' ")
if save == "Y"or"y":
	name = input('enter the file name-')
	f = open(name,"x+")
	f.write(password)
	f.close() 
	print('Done')
input()
