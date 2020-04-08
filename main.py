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
	print("Generating and writing to sauce.txt...")
	for i in range(sauceAmount):
		sauce = random.randint(100000, 299999) #There is some sauce that are >299999 but they're uncommon
		output.write(str(sauce) + "\n") #Writes the generated sauce to seperate lines in a .txt file
	output.close()
	print("WARNING: Keep in mind this is all random, some of the sauce may not work")
	print("There should be a .txt file with the sauce generated where this .py file is")
	while True:
		while True:
			answer = input("Open random sauce in your default web browser? WARNING: It will not open in a private/incognito window (y/n): ")
			if answer in ("y", "n"):
				break
			print("Please type y or n (case sensitive)")
		if answer == "y":
			outputRead = open("sauce.txt").read().splitlines()
			randomOpen = random.choice(outputRead)
			print("Opening " + str(randomOpen) + " in your default web browser...")
			webbrowser.open("https://nhentai.net/g/" + str(randomOpen), new=2)
			continue
		else:
			break

#What the user first sees
sauceAmount = sauceAmount("How much sauce do you want? ")
if sauceAmount <= 0:
	print("Please type something greater than 0")
else:
	generateSauce()