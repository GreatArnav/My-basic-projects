#! /usr/bin/env python3

from random import randint, choice, shuffle
import string
import time

print("Welcome to Arnav's password genretor")


while True:
	try:
		# variable
		num = int(input('Enter the number of number in the pasword-'))
		upper = int(input('Enter the number of upper case(capital letter) in password-'))
		lower = int(input('Enter the number of lower case(small letter) in pasword-'))
		special = input("Enter the special character[if you don't than enter 'n' to escape]-")
		small = 'abcdefghijklmnopqrstuvwxyz'
		capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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

		if special == 'n' or special == 'N':
			pass
		else:
			password = password+special

		print("\nYour password is ready - ",password,"\n\n")

		# Saving the password
		time.sleep(2)
		if password != "":
		
			save = input("If you want save password in file\nEnter the 'Y'\nIf not enter 'n' ")
			if save == "y"or save == 'Y':
				name = input('Enter the file name - ')
				f = open(name,"x+")
				f.write(password)
				f.close() 
				print('Done')
				break
			else:
				input()
				break
				

	except ValueError :
		print('Invalid Input\n')
		print('Try Again')

		continue






