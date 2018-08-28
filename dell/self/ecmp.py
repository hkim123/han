#!/usr/bin/python
from __future__ import print_function
import commands
import re

print("="*30)
print("Check multipath..........")
print("="*30)


prefix = raw_input("please enter prefix: ")
out = commands.getoutput('hshell -c "l3 defip show" | grep ' + prefix)
print(out)

multi_path = re.search('(2000*)',out)
#print(multi_path.group(0))

print(" ")
print("="*30)
print("Check next hop..........")
print("="*30)

cmd = 'hshell -c "l3 multipath show {}"'.format(multi_path.group(0))
print('CMD = '+cmd)

path = commands.getoutput(cmd)
print(path)

path_1 = path.splitlines()
#print(path_1)
#print(type(path_1))

path_2 = path_1[2]
#print(path_2)
#print(type(path_2))

path_3 = path_2.split()
#print(path_3)
path_3.pop(0)

#print(path_3)

for item in path_3:
	hshell_output = commands.getoutput('hshell -c "l3 egress show {}"'.format(item))
	print(hshell_output)

