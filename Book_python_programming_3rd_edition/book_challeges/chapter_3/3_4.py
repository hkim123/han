#! /usr/bin/env/python3

# 4.Here is bigger challenger. Write the pseudocode for a program where the player and computer trade place in the number guessing game. That is, the player picks a random number between 1 and 100 that the computer has to guess. Before you start, think about how you guess. if all goes well, try coding the game.

import random

guess = random.randint(1, 20)
print ("guess=", guess)
choice = int(input("If this is high enter 1, if this is low enter 2, if this is the number enter 3, "))


while choice != 3:
    if choice == 1:
        A = random.randint(1,guess-1)
        print("a=", A)
        choice = int(input("If this is high enter 4, if this is low enter 5, if this is the number enter 3,"))

    elif choice == 2:
        A = random.randint(guess, 20)
        print("a=", A)
        choice = int(input("If this is high enter 4, if this is low enter 5, if this is the number enter 3,"))

    elif choice == 4:
        B=random.randint(1,A-1)
        print("b=", B)
        choice = int(input("high enter 6, if this is low enter 7, if this is the number enter 3,"))

    elif choice == 5:
        B = random.randint(A,guess-1)
        print("b=", B)
        choice = int(input("high enter 6 : if this is low enter 7 if this is the number enter 3 :"))

    elif choice ==6:

        C = random.randint(1,B-1)
        print("c=", C)
        choice = int(input("high enter 8 : if this is low enter 9 if this is the number enter 3 :"))

    elif choice ==7:
        C = random.randint(B, A)
        print("c=", C)
        choice = int(input("high enter 8 : if this is low enter 9 if this is the number enter 3 :"))

    elif choice ==8:

        D = random.randint(1,C-1)
        print("d=", D)
        choice = int(input("high enter 10 : if this is low enter 11 if this is the number enter 3 :"))

    elif choice ==9:
        D = random.randint(B, C-1)
        print("d=", D)
        choice = int(input("high enter 10 : if this is low enter 11 if this is the number enter 3 :"))



print ("Yes, I got it !!!")



input("\n\nPress the enter key to exit.")


