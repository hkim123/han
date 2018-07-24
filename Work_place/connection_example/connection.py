#!/usr/bin/python

import os
from subprocess import *

print "please select device ?"

print "Super-Spine = 1 \n" "spine-1 = 2 \n" "spine-2 = 3 \n" "Leaf-1 = 4 \n" "Leaf-2 =5 \n" "Quagga = 6 \n"


while True:
	select = raw_input("please select device(1,2,3,4,5,6) : Quick(press q)")
#raw_inut = string, input is not a string.so if your input is raw input you should change select = ""
	if select == "1":
		os.system("ssh root@10.11.131.40")
		break

	elif select == "2":
		os.system("ssh root@10.11.131.44")
		break

	elif select == "3":
		os.system("ssh admin@10.11.131.39")
		break

	elif select == "4":
		os.system("ssh root@10.11.131.41")
		break

	elif select == "5":
		os.system("ssh root@10.11.131.42")
		break

	elif select == "6":
		#    	os.system("ssh root@10.11.131.37  ls -alt")
		#        os.system("ls -alt")
		#        os.system("pwd")
		#        os.system("ifconfig -a")
		#        os.system("ls ")
		#        Popen('ifconfig en0', shell=True)
		out = check_output('ssh root@10.11.131.37 ls -alt', shell=True)
		print out
		#        call ("ssh root@10.11.131.37 ls -alt", shell=True)
		#        call ("ls -alt", shell=True)
		break

	elif select == "q" :
		break

	else:
		print "You enter wrong value, please choose again.\n"
		continue
