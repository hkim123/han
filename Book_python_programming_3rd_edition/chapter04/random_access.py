# Random Access
# Demonstrates string indexing

import random

word = "index"
print("The word is: ", word, "\n")
#print (word[-1]) # it means last element for here it is x
#print (word[-2]) # means second last element, for here it is e
#print (word [-5]) # this is last one, ot start from right to left, right start -1, if you specify -6, will error
#print (word[0])  # all start from 0, for here it is i


high = len(word)  #this value is 4, because it start from let to right and start 0
low = -len(word)  #this value is -5, because it start from right to left and start -1

for i in range(10):
    position = random.randrange(low, high)
#    print (position)
    print("word [",position, "]\t", word[position])

input("\n\nPress the enter key to exit.")
