"""
Assignment Question 2/1
Author: Raforawesome
Due Date: Feb 17, 2022 11:59 PM
Question or problem: Option B - Input Checker
Class: ICS3UI-02
"""

import math  # import math library for number input validation


vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [
	'b', 'c', 'd', 'f', 'g',
	'h', 'j', 'k', 'l', 'm',
	'n', 'p', 'q', 'r', 's',
	't', 'v', 'w', 'x', 'y',
	'z'
]
affirmatives = ['y', 'yes']
negatives = ['n', 'no']

def is_decimal(num):  # function to streamline checking decimals
	return not num == math.floor(num)

def run():  # make a function and use recursion to repeat the program
	questions = [  # preset questions to ask, for efficient code
		"Enter a 4-digit whole number: ",
		"Enter an integer less than 50: ",
		"Enter a decimal number: ",
		"Enter a string that begins with a vowel: ",
		"Enter a string with a consonant: "
	]


	for i in range(1, len(questions) + 1):  # add one because range loops are exclusive
		question = questions[i - 1]  # subtract one to account for zero-indexing
		match i:  # only works in python 3.10+
			case 1:  # 4 digit whole number
				_input = input(question)  # prefix variable with underscore as 'input' already exists
				check = True  # start off being true
				message = ""  # make our message change depending on what exactly is wrong

				if not len(_input) == 4:  # our input must be 4 digits
					check = False
					message = "Input must be 4 characters!\n"

				if not _input.isnumeric() and check:  # check if our input consists of only numbers
					check = False
					message = "Whole numbers must be integers!\n"
				
				if check and not int(_input) >= 0:  # check if our number is above 0 (no negatives)
					check = False
					message = "Whole numbers must be positive!\n"

				if check:  # if none of those if statements set check to false, send success message
					message = "That works!\n"
				print(message)


			case 2:  # integer below 50
				_input = input(question)

				try:
					int(_input)
				except:
					print("This number isn't an integer.\n")
				else:
					num = int(_input)

					if num >= 50:
						print("This integer isn't below 50!\n")
					else:
						print("That works!\n")


			case 3:
				_input = input(question)
				
				try:
					float(_input)
				except:
					print('Provided input is not a valid float.\n')
				else:
					if is_decimal(float(_input)):
						print("That works!\n")
					else:
						print('This number is not a decimal.\n')


			case 4:
				_input = input(question)
				char = _input[:1]

				if char.lower() in vowels:
					print("That works!\n")
				else:
					print("The first character of this string is not a vowel!\n")


			case 5:
				_input = input(question)
				char = _input[:1]

				if char.lower() in consonants:
					print("That works!\n")
				else:
					print("The first character of this string is not a consonant!\n")


	rerun = True
	while True:
		_input = input("\nWould you like to repeat the program? [Y/n]  ")
		if _input.lower() in affirmatives:
			rerun = True
			break
		elif _input.lower() in negatives:
			rerun = False
			break
		else:
			print('Invalid input!')
			continue

	if rerun:
		print('\n')
		run()
	else:
		exit()

run()