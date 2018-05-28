#!/usr/bin/python
from subprocess import *
pro = ['ssh root@10.11.131.37']
#prog = ['ping','www.google.com']
prog = ['ssh','root@10.11.131.37']
pipe = Popen(prog)
#print '------'
#print pipe.stdout.read()
