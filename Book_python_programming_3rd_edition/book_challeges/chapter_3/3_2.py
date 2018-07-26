#! /usr/bin/env/python3

# 2.Write program that flip a coin 100 times and then tells you the number of head and tails.

import random

tries = 0
head = 0
tail = 0

while tries <= 99:
  coin = random.randint(1, 2)
  if coin == 1:
    head += 1
#    print("head is :",head)
  elif coin == 2:
    tail += 1
#    print("tail is :",tail)

  tries += 1
#  print("so far you tries :",tries)


print ("you have head", head, "times and tail", tail , "times")

input ("\n\n press enter key to exit")