#! /usr/bin/env/python3
# 1.Write program that simulates a fortune cookies.The program should display one of five unique fortune, at random,each time it's run

import random
fortune=random.randint(1,5)

print ("Today you will be fortune") 

if fortune == 1:
    print("\nyou will be healthy")

elif fortune == 2:
    print("\nyou will be rich")

elif fortune == 3:
    print("\nYou will be good day today")

elif fortune == 4:
    print("\nyou are handsome man")

elif fortune == 5:
    print("\nyou are so beautiful")

else:

    print("\nno way")

input("\n\n press enterkey to exit out") 
