#!/usr/bin/python
from __future__ import print_function
import subprocess
import commands
import re
import os
import pexpect

#PROMPT = ['~# ','[\r\n]*TMPR# ','>>>','> ','\$ ']
PROMPT = ['[\r\n]*OPX#']

def send_cmd(child,cmd):
        child.sendline(cmd)
        child.expect(cmd+'[\r\n]*')
#        child.expect(cmd+'[\n]*')
        child.expect(PROMPT)
        #print("match index: {}".format(i))
        #print(child.match)
        return(child.before)

def cnp_cli() :
        child = pexpect.spawn('cnp_cli')
        child.expect(PROMPT)
        return child



child = cnp_cli()
print('#################################################')
print('Check BGP neighborship ............')
print('#################################################','\n')

bgp_output = (send_cmd(child,'show bgp neighbors | include "BGP state = Established" | count'))
bgp_1 = re.search('Count:\s(\d+)',bgp_output)
print("Number of BGP Neighbor : ",bgp_1.group(1))

if bgp_1.group(1) == '4':
	print("PASS !!!! BGP neighbor is 4",'\n' )
else:
	print("FAIL >>>>> BGP neighbor is NOT 4",'\n')


#bgp_out = (send_cmd(child,'show bgp neighbors | include "BGP state = Established"'))

print('#################################################')
print('Check OSPFv2 neighborship ............')
print('#################################################','\n')

ospf_output = (send_cmd(child,'show ospfv2 neighbor | include FULL | count'))
ospf_1 = re.search('Count:\s(\d+)',ospf_output)
print("Number of OSPF Neighbor : ",ospf_1.group(1))

if ospf_1.group(1) == '6' :
	print("PASS !!!!!!   OSPF neighbor is 6",'\n')
else :
	print("FAIL >>>>>>> OSPF neighbor is NOT 6",'\n') 


#ospf_out = (send_cmd(child,'show ospfv2 neighbor'))
#print(version)
#print(bgp_output)
#print(bgp_out)
#print(ospf_output)
#print(ospf_out)

