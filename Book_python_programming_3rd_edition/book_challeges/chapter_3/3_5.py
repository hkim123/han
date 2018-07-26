#! /usr/bin/env/python3

print("\tWelcome to the NEW 'Guess My Number'!")
print("\nThis time we will switch seats! You may pick a number between 1 and 10.")
print("And the PC will try to guess it in less then 10 attempts.\n")

import random
# Set the initial values
user_number = int(input("Pick a number between 1 and 10: "))
times = 1
pc_guess = random.randint(1, 10)

# The while loop is used to compare the user_number to the pc_guess
while pc_guess != user_number: # when the numbers are not the same run the while loop
    times+=1 # add 1 to the attempts of the PC
    if times>10: # When the PC has guessed more then 10 times, congratulate the user and break the while loop
        print("You win!! It took the PC more then 10 attempts to guess your number!!\n")
        break
    pc_guess = random.randint(1, 10) # give a new value to pc_guess
    print("Is it", pc_guess,"?")
    print("No.")

if pc_guess == user_number: #if the guessed number is correct print the following lines:
    print("The PC guessed it! The number was", user_number)
    print("It took", times, "tries!\n")
    print("End of the NEW Guess My Number game, I hope you enjoyed it!\n\n")

#exit statement
input("\n\nPress the enter key to exit.")
