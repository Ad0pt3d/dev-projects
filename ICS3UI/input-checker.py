"""
Assignment Question 2/1
Author: Raforawesome
Due Date: Feb 17, 2022 11:59 PM
Question or problem: Option B - Input Checker
Class: ICS3UI-02
"""

import math  # import math library for number input validation


def is_decimal(num):  # function to streamline checking decimals
	return num == math.floor(num)

def run():  # make a function and use recursion to repeat the program
	questions = [  # preset questions to ask, for efficient code
		"Enter a 4-digit whole number: ",
		"Enter an integer lessx than 50: ",
		"Enter a decimal number: ",
		"Enter a string that begins with a vowel: ",
		"Enter a string with a consonant: "
	]


	for i in range(1, len(questions) + 1):  # add one because range loops are exclusive
		question = questions[i - 1]  # subtract one to account for zero-indexing
		match i:  # only works in python 3.10+
			case 1:
				_input = input(question)  # prefix variable with underscore as 'input' already exists
				check = True  # start off being true
				message = ""  # make our message change depending on what exactly is wrong

				if not len(_input) == 4:  # our input must be 4 digits
					check = False
					message = "Input must be 4 characters!"

				if not _input.isnumeric() and check:  # check if our input consists of only numbers
					check = False
					message = "Whole numbers must be integers!"
				
				if check and not int(_input) >= 0:  # check if our number is above 0 (no negatives)
					check = False
					message = "Whole numbers must be positive!"

				if check:  # if none of those if statements set check to false, send success message
					message = "That works!"
				print(message)


			case 2:
				_input = input(question)
				check = True
				isint = False
				message = ""
				

run()