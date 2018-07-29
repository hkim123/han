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

print ("%15s%15s" % ('Local_interface','Remote_interface'))
print ("---" * 20)
print ("Local_interface" ," " * 25 ,"Remote_interface")
print ("---" * 20)

print("%15s%15s" % ('Local_int','Remote_int'))
print("%15s%15s" % ('=========','=========='))
#row_list = []
for (local_inf, remote_inf) in zip(local_int, remote_int):
	print("%15s%15s" % (local_inf, remote_inf))

# for (kernel_port, hw_port, logical_port, bcm_port) in zip(kernel_intf_list, hw_port_list, logical_port_list,bcm_port_list):
# 	print("%15s%15s%15s%15s" % (kernel_port, hw_port, logical_port, bcm_port))
#
# for item in local_int :
#     print (item)
# for item1 in remote_int:
#     print (item1)
