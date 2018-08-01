#!/usr/bin/python
from __future__ import print_function
import subprocess
import commands
import re

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
                print ("\n""WARNING >>>>>> ", proc,">>>>>>>>is NOT ACTIVE !!!","\n")

print("###############################################")
print("CHECK OPX SERVICES ........")
print("###############################################")

opx_output=commands.getoutput('opx-show-system-status')
print(opx_output)
opx_output_1 = re.search('running',opx_output)


if opx_output_1 :
	print ("\n","PASS!!! opx has no degrade process","\n")
else :
	print("\n","WARNING >>>>>> opx has degrade !!!!","\n")

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
        print("\n""WARNING>>>>>>>> DISK Space is full more than 80% !!!!""\n")
	print("Disk Usage: ",usage,"%""\n")



print("###############################################")
print("CHECK CPU Usage.........")
print("###############################################")

cpu_output = commands.getoutput('mpstat')
cpu_idle = re.search('all.*\s(\d.*)',cpu_output)
cpu_usage = 100 - float(cpu_idle.group(1))

if cpu_usage > 70 :
	print ("\n""WARNING>>>>>>>>>>>>>>CPU usage is more than 70% !!!!! ""\n")
        print("\n""CPU Usage: ",cpu_usage,"%""\n")

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
	print("Total memory: ", memory_usage.group(1),"    Free memory : ", memory_usage.group(3))
else :
	print("\n""WARNING>>>>>>>>> Memory usage is more than 70%""\n")
	print("Free memory : ",mem_free,"%")
 	print("Total memory: ", memory_usage.group(1),"    Free memory : ", memory_usage.group(3))
