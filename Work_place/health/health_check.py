#!/usr/bin/python
from __future__ import print_function
import subprocess
import commands
import re
import pexpect
from termcolor import colored, cprint

normal = '\033[0m'
failwarning = '\033[93m'

print("###############################################")
print("CHECK MSW/OPX PROCESS ........")
print("###############################################")

process = ['nbased','pymm','ymm','confd','opx-pas','opx-nas']
for proc in process:
       	#systemctl_output=subprocess.check_output(['systemctl', 'status', proc])
        systemctl_output=commands.getoutput('systemctl status %s' % proc)
#        print(systemctl_output)

        output_1 = re.search('Active:\s+active\s+\(running\)',systemctl_output)
        #print(output_1)
        if output_1 :
            print ("\n","PASS!!!",proc,"is active","\n")
        else:
            print(failwarning)
            print ("\n""WARNING >>>>>> ", proc,">>>>>>>>is NOT ACTIVE !!!","\n")
            print(normal)

print("###############################################")
print("CHECK OPX SERVICES ........")
print("###############################################")

opx_output=commands.getoutput('opx-show-system-status')
print(opx_output)
opx_output_1 = re.search('running',opx_output)


if opx_output_1 :
    print ("\n","PASS!!! opx has no degrade process","\n")
else :
    print(failwarning)
    print("\n","WARNING >>>>>> opx has degrade !!!!","\n")
    print(normal)

print("###############################################")
print("CHECK DISK SPACE.........")
print("###############################################")

disk_output = commands.getoutput('df -h')
print("\n",disk_output,"\n")
disk_usage = re.search('(\d+)\%',disk_output)

#print(disk_usage.group(1))
usage = float(disk_usage.group(1))
#print (usage)

if usage < 80 :
    print("\n""PASS!!!!  DISK Usage is less than 80%""\n")
    print("Disk Usage: ",usage,"%""\n")
else :
    print(failwarning)
    print("\n""WARNING>>>>>>>> DISK Space is full more than 80% !!!!""\n")
    print("Disk Usage: ",usage,"%""\n")
    print(normal)

print("###############################################")
print("CHECK CPU Usage.........")
print("###############################################")

cpu_output = commands.getoutput('mpstat')
cpu_idle = re.search('all.*\s(\d.*)',cpu_output)
cpu_usage = 100 - float(cpu_idle.group(1))

if cpu_usage > 70 :
    print(failwarning)
    print ("\n""WARNING>>>>>>>>>>>>>>CPU usage is more than 70% !!!!! ""\n")
    print("\n""CPU Usage: ",cpu_usage,"%""\n")
    print(normal)

else :
    print("\n""PASS!!!! CPU usage is less than 70%")
    print("\n""CPU Usage: ",cpu_usage,"%""\n")

print("###############################################")
print("CHECK Memory Usage.........")
print("###############################################")

memory_output = commands.getoutput('free -m')
memory_usage = re.search('Mem:\s+(\d+)\s+(\d+)\s+(\d+)',memory_output)
print(memory_output)
#print(memory_usage.group(1))
#print(memory_usage.group(3))

mem_free = float(memory_usage.group(3))/float(memory_usage.group(1)) * 100
print (mem_free)

if mem_free > 30 :
    print("\n""PASS!!!!! Memory usage is less than 30%""\n")
    print("Free Memory : ", mem_free,"%")
    print("Total memory: ", memory_usage.group(1),"    Free memory : ", memory_usage.group(3),"\n")
else :
    print(failwarning)
    print("\n""WARNING>>>>>>>>> Memory usage is more than 70%""\n")
    print("Free memory : ",mem_free,"%")
    print("Total memory: ", memory_usage.group(1),"    Free memory : ", memory_usage.group(3),"\n")
    print(normal)

############################## Metaswitch stack check protocl #################

PROMPT = ['[\r\n]*OPX#']

def cnp_cli() :
        child = pexpect.spawn('cnp_cli')
        child.expect(PROMPT)
        return child

child = cnp_cli()
print('#################################################')
print('Check BGP neighborship ............')
print('#################################################','\n')

child.sendline('show bgp neighbors | include "BGP state = Established"')
child.expect(PROMPT)
print ('\n'.join(child.before.strip().splitlines()[0:]),'\n')

child.sendline('show bgp neighbors | include "BGP state = Established" | count')
child.expect(PROMPT)

bgp_output = ('\n'.join(child.before.strip().splitlines()[1:]))
#print(bgp_output)
bgp_1 = re.search('Count:\s(\d+)',bgp_output)
print("Number of BGP Neighbor : ",bgp_1.group(1),'\n')

if bgp_1.group(1) == '8':
    print("PASS !!!! BGP neighbor is 8",'\n' )
else:
    cprint("FAIL >>>>>>  FAIL >>>>  FAIL >>>>>>> BGP neighbor is NOT 8",'yellow',attrs=['blink'])
    print('\n')

print('#################################################')
print('Check OSPFv2 neighborship ............')
print('#################################################','\n')

child.sendline('show ospfv2 neighbor | include FULL')
child.expect(PROMPT)
print ('\n'.join(child.before.strip().splitlines()[0:]),'\n')

child.sendline('show ospfv2 neighbor | include FULL | count')
child.expect(PROMPT)

ospf_output = ('\n'.join(child.before.strip().splitlines()[0:]))

ospf_1 = re.search('Count:\s(\d+)',ospf_output)
print("Number of OSPF Neighbor : ",ospf_1.group(1),'\n')

if ospf_1.group(1) == '6' :
    print("PASS !!!!!!   OSPF neighbor is 6",'\n')
else :
    cprint("FAIL >>>>>>  FAIL >>>>  FAIL >>>>>>> OSPF neighbor is NOT 6",'yellow',attrs=['blink'])
    print('\n')
