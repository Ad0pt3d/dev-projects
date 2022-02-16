"""
Assignment Question 2/1
Author: Raforawesome
Due Date: Feb 17, 2022 11:59 PM
Question or problem: Option B - Input Checker
Class: ICS3UI-02
"""

import math  # import math library for number input validation


def is_decimal(num):
	return num == math.floor(num)

def run():  # make a function and use recursion to repeat the program
	questions = [  # preset questions to ask, for efficient code
		"Enter a 4-digit whole number: ",
		"Enter an integer less than 50: ",
		"Enter a decimal number: ",
		"Enter a string that begins with a vowel: ",
		"Enter a string with a consonant: "
	]

	inputs = []  # where we store our ordered inputs


	for question in questions:
		inputs.append(input(question))

	for i in range(1, len(questions) + 1):  # add one because range loops stop 
		match i:
			case 1:
				check, error = ""





# run()