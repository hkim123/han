#!/usr/bin/python
import subprocess
import re
import commands

#lldpctl_output = subprocess.check_output(["lldpctl"])
lldpctl_output = commands.getoutput('lldpctl')

local_int = re.findall('Interface:\s+(e\d+-\d+-\d*)', lldpctl_output)
remote_int = re.findall('ifname\s+(e\d+-\d+-\d)',lldpctl_output)
remote_ip = re.findall('MgmtIP:\s+(\d+.\d+.\d+.\d+)',lldpctl_output)
vlan_info = re.findall('VLAN:\s+(\d+)',lldpctl_output)
link_agg = re.findall('(bnd\d+.\d+)',lldpctl_output)
#print(lldpctl_output)
#print("local_int: ",local_int)
#print("remote_int: ",remote_int)
#print("remote_ip: ",remote_ip)
#print("vlan: ",vlan_info)
#print("link-agg: ",link_agg)


print ("{0:>15s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}".format('local_int','remote_int','remote_ip','vlan_info','link_agg'))
print ("{0:>15s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}".format('=========','==========','==========','========','======='))

for (local_inf, remote_inf, remote_ip, vlan_info,link_agg) in zip(local_int, remote_int, remote_ip, vlan_info, link_agg):
	print("{0:>15s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}".format(local_inf, remote_inf, remote_ip, vlan_info,link_agg))


