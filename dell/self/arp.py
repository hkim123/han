#!/usr/bin/python
from __future__ import print_function
import subprocess
import commands
import datetime
import time

while True :
	arp = commands.getoutput('ip neighbor show | grep REACHABLE | wc')
	print(arp,end = '           ');print(datetime.datetime.now())
	#print(datetime.datetime.now())
	time.sleep(2)

