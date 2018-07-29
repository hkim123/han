import subprocess
import re

output = '''
Interface:    e101-001-1, via: LLDP, RID: 2, Time: 0 day, 20:29:41
  Chassis:     
    ChassisID:    mac 86:59:e9:64:f3:84
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.44
    MgmtIP:       fe80::f68e:38ff:fe68:1b47
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-013-0
    PortDescr:    NAS## 0 49
    Port is aggregated. PortAggregID: 15
  VLAN:         9 bnd9.9
-------------------------------------------------------------------------------
Interface:    e101-002-1, via: LLDP, RID: 2, Time: 0 day, 20:29:41
  Chassis:     
    ChassisID:    mac 86:59:e9:64:f3:84
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.44
    MgmtIP:       fe80::f68e:38ff:fe68:1b47
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-014-0
    PortDescr:    NAS## 0 53
    Port is aggregated. PortAggregID: 15
  VLAN:         9 bnd9.9
  '''
#local_int =[]

local_int = re.findall('Interface:\s+(e\d+-\d+-\d*)', output)
remote_int = re.findall('ifname\s+(e\d+-\d+-\d)',output)
vlan_info = re.findall('VLAN:\s+(\d)',output)
link_agg = re.findall('(bnd\d.\d)',output)
#print ("local_interface: ", local_int.group())
print (local_int)
print (remote_int)
print (vlan_info)
print (link_agg)

# print ("%s%20s" % ('Local_interface','Remote_interface'))
# print ("{0:15s}{1:15s}".format('local_int','remote_int'))
# print ("---" * 20)
# print ("Local_interface" ," " * 25 ,"Remote_interface")
# print ("---" * 20)

# print("%15s%15s" % ('Local_int','Remote_int'))
# print("%15s%15s" % ('=========','=========='))
# #row_list = []
# for (local_inf, remote_inf) in zip(local_int, remote_int):
# 	print("%15s%15s" % (local_inf, remote_inf))

print ("{0:>15s}{1:>15s}".format('local_int','remote_int'))
print ("{0:>15s}{1:>15s}".format('=========','=========='))

for (local_inf, remote_inf) in zip(local_int, remote_int):
	print("{0:>15s}{1:>15s}".format(local_inf,remote_inf))


# print ("{0:10}".format('test'))
# print ("{0:<10}".format('test'))
# print("%s"%('test'))
#
# print ("{0:>10}".format('test'))
#
# #print("%s"%('test'))
# print("%10s"%('test'))
#
# print ("{0:<15} Python!!".format('hello'))
# print ("%6s Python!!" %"hello")
# print ("{0:^10}".format('hello'))


# alist = ['a1', 'a2', 'a3']
#
# for i, a in enumerate(alist):
#     print (i, a)