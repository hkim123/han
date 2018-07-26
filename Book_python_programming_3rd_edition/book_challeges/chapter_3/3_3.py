#! /usr/bin/env/python3

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while tries <= 6:
	if guess == the_number:
		print ("yes, you are correct")
	elif guess > the_number:
		print ("lower .. ")
	elif guess < the_number:
		print("higher..") 
	tries += 1
	guess = int(input("Take a guess: "))




#print("You guessed it!  The number was", the_number)
#print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")

