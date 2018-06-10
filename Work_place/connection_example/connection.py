#!/usr/bin/python

import os
from subprocess import *

print "please select device ?"

print "Super-Spine = 1 \n" "spine-1 = 2 \n" "spine-2 = 3 \n" "Leaf-1 = 4 \n" "Leaf-2 =5 \n" "Quagga = 6 \n"



select = input("please select device(1,2,3,4,5,6) : ")

if select == 1:
	os.system("ssh root@10.11.131.40")

elif select == 2:
	os.system("ssh 10.11.131.44")

elif select == 3:
	os.system("ssh admin@10.11.131.39")

elif select == 4:
	os.system("ssh 10.11.131.41")

elif select == 5:
	os.system("ssh 10.11.131.42")

elif select == 6:
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
else:
	print "You enter wrong value, please restart scrip"



