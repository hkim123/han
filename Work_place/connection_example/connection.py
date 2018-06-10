#!/usr/bin/python
import os

print "Which server would you like to login"
select = input("Please choose server!!! ")

if select == 1 :
  os.system("ssh root@10.11.131.37")
elif select == 2 :
  os.system("ssh root@10.11.131.40")
else :
  print "you have to choose 1 or 2, please try again"
