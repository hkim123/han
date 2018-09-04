#!/usr/bin/python
from __future__ import print_function
import commands
import subprocess
import re

#prefix = raw_input("please enter prefix: ")

#out = commands.getoutput('hshell -c "l3 defip show" | grep ' + prefix)

out = commands.getoutput('hshell -c "l3 defip show" | grep 13.0.1.0')
print(out)


multi_path = re.search('(2000*).*(ECMP)',out)
if multi_path.group(1) and  multi_path.group(2):

	print('ECMP is working')
	print(multi_path.group(1))
#	print(multi_path.group(2))
else:
	print('ECMP does not working')
#	break

path = commands.getoutput('hshell -c "l3 multipath show" ' + multi_path.group(1))
print(path)

next_hop = re.search('Interfaces:\s+(\d+)\s(\d+)',path)
#print(next_hop)

#print(next_hop.group(1))
#print(next_hop.group(2))


next_hop_1 = commands.getoutput('hshell -c "l3 egress show "' + next_hop.group(1))
print(next_hop_1)
next_hop_2 = commands.getoutput('hshell -c "l3 egress show "' + next_hop.group(2))
print(next_hop_2)
