#!/usr/bin/python
from subprocess import *
pro = 'ping'
target='www.google.com'
p=Popen([pro,target])
call([pro,target])
