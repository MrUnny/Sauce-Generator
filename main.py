import random
import webbrowser

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
	output.close()
	print("WARNING: Keep in mind this is all random, some of the sauce may not work")
	print("There should be a .txt file with the sauce generated where this .py file is")
	while True:
		while True:
			answer = raw_input("Open random sauce in default web browser? WARNING: It will not open in a private window (y/n): ")
			if answer in ("y", "n"):
				break
			print("Please type y or n (case sensitive)")
		if answer == "y":
			outputRead = open("sauce.txt").read().splitlines()
			randomOpen = random.choice(outputRead)
			print("Opening " + str(randomOpen) + " in your default web browser...")
			webbrowser.open("https://nhentai.net/g/" + str(randomOpen), new=2)
			break
		else:
			break

#MAIN PROGRAM
sauceAmount = sauceAmount("How much sauce do you want? ")
if sauceAmount > 200000:
	print("Whoa, that's too much sauce, you'll get repeats and that's no good")
elif sauceAmount <= 0:
	print("Exiting...")
else:
	generateSauce()
