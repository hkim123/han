# No Vowels
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"  #variable is upper case means constant and refer to a value that is not mean to change

print()
for letter in message:
    if letter.lower() not in VOWELS:
        print(letter.upper())       #whatever letter in input chage to low case, even if user input is upper case,
                                    # it change to low case and cmpare to VOWEL
        new_message += letter
        print("A new string has been created:", new_message)

print("\nYour message without vowels is:", new_message)

input("\n\nPress the enter key to exit.")

