import random
import os

def sauceAmount(amount):
	while True:
		try:
			userInput = int(input(amount))
		except ValueError:
			print("Only whole numbers are allowed")
			continue
		else:
			return userInput
			break

def generateSauce():
	output = open("sauce.txt", "a+") #Creates a file called sauce.txt next to the .py file
	for i in range(sauceAmount):
		sauce = random.randint(100000, 299999) #There is some sauce that are >299999 but they're uncommon
		print(sauce)
		output.write(str(sauce) + "\n") #Writes the generated sauce to seperate lines in a .txt file
	print("WARNING: Keep in mind this is all random, some of the sauce may not work")
	print("There should be a .txt file with the sauce generated where this .py file is")

#MAIN PROGRAM
sauceAmount = sauceAmount("How much sauce do you want? ")
if sauceAmount > 200000:
	print("Whoa, that's too much sauce, you'll get repeats and that's no good")
else:
	generateSauce()
