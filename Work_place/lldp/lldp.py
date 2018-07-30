import subprocess
import re

output = '''
-------------------------------------------------------------------------------
LLDP neighbors:
-------------------------------------------------------------------------------
Interface:    eth0, via: LLDP, RID: 1, Time: 0 day, 02:14:39
  Chassis:     
    ChassisID:    mac 00:01:e8:95:f7:f2
    TTL:          120
  Port:        
    PortID:       ifname GigabitEthernet 0/11
-------------------------------------------------------------------------------
Interface:    e101-013-0, via: LLDP, RID: 4, Time: 0 day, 02:12:44
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-001-1
    PortDescr:    NAS## 0 49
    Port is aggregated. PortAggregID: 5
  VLAN:         9 bnd9.9
-------------------------------------------------------------------------------
Interface:    e101-014-0, via: LLDP, RID: 4, Time: 0 day, 02:12:44
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-002-1
    PortDescr:    NAS## 0 53
    Port is aggregated. PortAggregID: 5
  VLAN:         9 bnd9.9
-------------------------------------------------------------------------------
Interface:    e101-015-0, via: LLDP, RID: 4, Time: 0 day, 02:12:44
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-003-1
    PortDescr:    NAS## 0 57
    Port is aggregated. PortAggregID: 6
  VLAN:         10 bnd10.10
-------------------------------------------------------------------------------
Interface:    e101-016-0, via: LLDP, RID: 4, Time: 0 day, 02:12:44
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-004-1
    PortDescr:    NAS## 0 61
    Port is aggregated. PortAggregID: 6
  VLAN:         10 bnd10.10
-------------------------------------------------------------------------------
Interface:    e101-029-0, via: LLDP, RID: 4, Time: 0 day, 02:12:11
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-017-1
    PortDescr:    NAS## 0 97
    Port is aggregated. PortAggregID: 7
  VLAN:         11 bnd11.11
-------------------------------------------------------------------------------
Interface:    e101-030-0, via: LLDP, RID: 4, Time: 0 day, 02:12:11
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-018-1
    PortDescr:    NAS## 0 101
    Port is aggregated. PortAggregID: 7
  VLAN:         11 bnd11.11
-------------------------------------------------------------------------------
Interface:    e101-031-0, via: LLDP, RID: 4, Time: 0 day, 02:11:47
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-019-1
    PortDescr:    NAS## 0 105
    Port is aggregated. PortAggregID: 8
  VLAN:         12 bnd12.12
-------------------------------------------------------------------------------
Interface:    e101-032-0, via: LLDP, RID: 4, Time: 0 day, 02:11:47
  Chassis:     
    ChassisID:    mac d6:c6:8e:d5:97:c3
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.40
    MgmtIP:       fe80::3617:ebff:fe45:e880
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-020-1
    PortDescr:    NAS## 0 109
    Port is aggregated. PortAggregID: 8
  VLAN:         12 bnd12.12
-------------------------------------------------------------------------------
Interface:    e101-001-2, via: LLDP, RID: 2, Time: 0 day, 02:12:42
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-049-2
    PortDescr:    NAS## 0 102
    Port is aggregated. PortAggregID: 76
  VLAN:         2 bnd2.2
-------------------------------------------------------------------------------
Interface:    e101-001-3, via: LLDP, RID: 2, Time: 0 day, 02:12:45
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-049-3
    PortDescr:    NAS## 0 103
    Port is aggregated. PortAggregID: 77
  VLAN:         3 bnd3.3
-------------------------------------------------------------------------------
Interface:    e101-001-4, via: LLDP, RID: 2, Time: 0 day, 02:12:45
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-049-4
    PortDescr:    NAS## 0 104
    Port is aggregated. PortAggregID: 77
  VLAN:         3 bnd3.3
-------------------------------------------------------------------------------
Interface:    e101-002-1, via: LLDP, RID: 6, Time: 0 day, 00:40:41
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-001-0
    PortDescr:    NAS## 0 45
    Port is aggregated. PortAggregID: 7
  VLAN:         6 bnd6.6
-------------------------------------------------------------------------------
Interface:    e101-002-2, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-002-0
    PortDescr:    NAS## 0 46
    Port is aggregated. PortAggregID: 7
  VLAN:         6 bnd6.6
-------------------------------------------------------------------------------
Interface:    e101-002-3, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-003-0
    PortDescr:    NAS## 0 47
    Port is aggregated. PortAggregID: 7
  VLAN:         6 bnd6.6
-------------------------------------------------------------------------------
Interface:    e101-002-4, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-004-0
    PortDescr:    NAS## 0 48
    Port is aggregated. PortAggregID: 7
  VLAN:         6 bnd6.6
-------------------------------------------------------------------------------
Interface:    e101-017-1, via: LLDP, RID: 2, Time: 0 day, 02:12:45
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-050-1
    PortDescr:    NAS## 0 97
    Port is aggregated. PortAggregID: 78
  VLAN:         4 bnd4.4
-------------------------------------------------------------------------------
Interface:    e101-017-2, via: LLDP, RID: 2, Time: 0 day, 02:12:45
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-050-2
    PortDescr:    NAS## 0 98
    Port is aggregated. PortAggregID: 78
  VLAN:         4 bnd4.4
-------------------------------------------------------------------------------
Interface:    e101-017-3, via: LLDP, RID: 2, Time: 0 day, 02:12:45
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-050-3
    PortDescr:    NAS## 0 99
    Port is aggregated. PortAggregID: 79
  VLAN:         5 bnd5.5
-------------------------------------------------------------------------------
Interface:    e101-017-4, via: LLDP, RID: 2, Time: 0 day, 02:12:09
  Chassis:     
    ChassisID:    mac 36:06:84:33:bd:cb
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.41
    MgmtIP:       fe80::e6f0:4ff:fe07:65f9
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-050-4
    PortDescr:    NAS## 0 100
    Port is aggregated. PortAggregID: 79
  VLAN:         5 bnd5.5
-------------------------------------------------------------------------------
Interface:    e101-018-1, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-017-0
    PortDescr:    NAS## 0 25
    Port is aggregated. PortAggregID: 8
  VLAN:         7 bnd7.7
-------------------------------------------------------------------------------
Interface:    e101-018-2, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-018-0
    PortDescr:    NAS## 0 26
    Port is aggregated. PortAggregID: 8
  VLAN:         7 bnd7.7
-------------------------------------------------------------------------------
Interface:    e101-018-3, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-019-0
    PortDescr:    NAS## 0 27
    Port is aggregated. PortAggregID: 8
  VLAN:         7 bnd7.7
-------------------------------------------------------------------------------
Interface:    e101-018-4, via: LLDP, RID: 6, Time: 0 day, 00:40:40
  Chassis:     
    ChassisID:    mac ee:10:d3:bc:d7:6d
    SysName:      OPX
    SysDescr:     Debian GNU/Linux 8 (jessie) Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.43-2+deb8u2 (2017-06-14) x86_64
    TTL:          120
    MgmtIP:       10.11.131.42
    MgmtIP:       fe80::6600:6aff:fef7:14f4
    Capability:   Bridge, on
    Capability:   Router, on
    Capability:   Wlan, off
    Capability:   Station, off
  Port:        
    PortID:       ifname e101-020-0
    PortDescr:    NAS## 0 28
    Port is aggregated. PortAggregID: 8
  VLAN:         7 bnd7.7
-------------------------------------------------------------------------------
  '''

#output = subprocess.check_output(["lldpctl"])
local_int = re.findall('Interface:\s+(e\d+-\d+-\d*)', output)
remote_int = re.findall('ifname\s+(e\d+-\d+-\d)',output)
remote_ip = re.findall('MgmtIP:\s+(\d+.\d+.\d+.\d+)',output)
vlan_info = re.findall('VLAN:\s+(\d+)',output)
link_agg = re.findall('(bnd\d+.\d+)',output)
#print ("local_interface: ", local_int.group())
print (local_int)
print (remote_int)
print(remote_ip)
print (vlan_info)
print (link_agg)

print ("{0:>15s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}".format('local_int','remote_int','remote_ip','vlan_info','link_agg'))
print ("{0:>15s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}".format('=========','==========','==========','========','======='))

for (local_inf, remote_inf, remote_ip, vlan_info,link_agg) in zip(local_int, remote_int, remote_ip, vlan_info, link_agg):
	print("{0:>15s}{1:>15s}{2:>15s}{3:>15s}{4:>15s}".format(local_inf, remote_inf, remote_ip, vlan_info,link_agg))

# print (local_int)
# print (remote_int)
# print(remote_ip)
# print (vlan_info)
# print (link_agg)

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

# print ("{0:>15s}{1:>15s}{2:>15s}".format('local_int','remote_int','remote_ip'))
# print ("{0:>15s}{1:>15s}{2:>15s}".format('=========','==========','=========='))
#
# for (local_inf, remote_inf, remote_ip) in zip(local_int, remote_int, remote_ip):
# 	print("{0:>15s}{1:>15s}{2:>15s}".format(local_inf, remote_inf, remote_ip))


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