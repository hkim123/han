import re

output = """
bnd2      Link encap:Ethernet  HWaddr 64:00:6a:f7:15:09  
          UP BROADCAST RUNNING MASTER MULTICAST  MTU:1500  Metric:1
          RX packets:97219 errors:0 dropped:35 overruns:0 frame:0
          TX packets:96967 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:12977539 (12.3 MiB)  TX bytes:14713264 (14.0 MiB)

bnd3      Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f9  
          UP BROADCAST RUNNING MASTER MULTICAST  MTU:1500  Metric:1
          RX packets:97208 errors:0 dropped:28 overruns:0 frame:0
          TX packets:96978 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:12908760 (12.3 MiB)  TX bytes:14716538 (14.0 MiB)

bnd6      Link encap:Ethernet  HWaddr 42:c3:6f:2c:6b:af  
          UP BROADCAST MASTER MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

bnd7      Link encap:Ethernet  HWaddr 7e:16:00:a2:53:56  
          UP BROADCAST MASTER MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

bnd2.2    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:3f  
          UP BROADCAST RUNNING PROMISC ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:28441 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28370 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:2252888 (2.1 MiB)  TX bytes:2461448 (2.3 MiB)

bnd3.3    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:40  
          UP BROADCAST RUNNING PROMISC ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:28444 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28379 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:2254858 (2.1 MiB)  TX bytes:2464474 (2.3 MiB)

bnd6.6    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:43  
          UP BROADCAST PROMISC ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:290 (290.0 B)

bnd7.7    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:44  
          UP BROADCAST PROMISC ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:200 (200.0 B)

dummy0    Link encap:Ethernet  HWaddr 42:46:51:d5:74:26  
          inet6 addr: fe80::4046:51ff:fed5:7426/64 Scope:Link
          UP BROADCAST RUNNING NOARP  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8591 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:1890020 (1.8 MiB)

e101-001-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f5  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-002-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f6  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-003-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f7  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-004-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f8  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-005-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f9  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:28536 errors:0 dropped:0 overruns:0 frame:0
          TX packets:44160 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3638474 (3.4 MiB)  TX bytes:5150677 (4.9 MiB)

e101-006-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f9  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:22912 errors:0 dropped:0 overruns:0 frame:0
          TX packets:17214 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3087242 (2.9 MiB)  TX bytes:3150247 (3.0 MiB)

e101-007-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f9  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:22855 errors:0 dropped:0 overruns:0 frame:0
          TX packets:18454 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3090922 (2.9 MiB)  TX bytes:3267475 (3.1 MiB)

e101-008-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f9  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:22905 errors:0 dropped:0 overruns:0 frame:0
          TX packets:17150 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3092122 (2.9 MiB)  TX bytes:3148139 (3.0 MiB)

e101-017-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:05  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-018-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:06  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-019-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:07  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-020-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:08  
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-021-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:09  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:28534 errors:0 dropped:1 overruns:0 frame:0
          TX packets:45296 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3653644 (3.4 MiB)  TX bytes:5254125 (5.0 MiB)

e101-022-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:09  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:22916 errors:0 dropped:0 overruns:0 frame:0
          TX packets:17211 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3112667 (2.9 MiB)  TX bytes:3149969 (3.0 MiB)

e101-023-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:09  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:22915 errors:0 dropped:0 overruns:0 frame:0
          TX packets:17310 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3110634 (2.9 MiB)  TX bytes:3161031 (3.0 MiB)

e101-024-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:09  
          UP BROADCAST RUNNING SLAVE MULTICAST  MTU:1500  Metric:1
          RX packets:22854 errors:0 dropped:0 overruns:0 frame:0
          TX packets:17150 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:3100594 (2.9 MiB)  TX bytes:3148139 (3.0 MiB)

e101-041-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:1d  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8591 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:2147750 (2.0 MiB)

e101-041-0.13 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:1d  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-047-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:23  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8591 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:2147750 (2.0 MiB)

e101-047-0.12 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:23  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

e101-048-0 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:24  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:34337 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:3846890 (3.6 MiB)

e101-048-0.10 Link encap:Ethernet  HWaddr 64:00:6a:f7:15:24  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:25746 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:2008092 (1.9 MiB)

eth0      Link encap:Ethernet  HWaddr 64:00:6a:f7:14:f4  
          inet addr:10.11.131.42  Bcast:10.11.131.255  Mask:255.255.255.0
          inet6 addr: fe80::6600:6aff:fef7:14f4/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:205870 errors:0 dropped:0 overruns:0 frame:0
          TX packets:13397 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:500 
          RX bytes:25707182 (24.5 MiB)  TX bytes:3402374 (3.2 MiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:4932436 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4932436 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:264561167 (252.3 MiB)  TX bytes:264561167 (252.3 MiB)

npu-0     Link encap:Ethernet  HWaddr 92:af:e9:12:ab:92  
          BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

vlan2     Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:192.168.0.101  Bcast:0.0.0.0  Mask:255.255.255.252
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:28441 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28440 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:2139620 (2.0 MiB)  TX bytes:2464380 (2.3 MiB)

vlan3     Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:192.168.0.97  Bcast:0.0.0.0  Mask:255.255.255.252
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:28444 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28449 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:2141582 (2.0 MiB)  TX bytes:2467338 (2.3 MiB)

vlan6     Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:192.168.0.65  Bcast:0.0.0.0  Mask:255.255.255.252
          UP BROADCAST PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:200 (200.0 B)

vlan7     Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:192.168.0.69  Bcast:0.0.0.0  Mask:255.255.255.252
          UP BROADCAST PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:110 (110.0 B)

vlan10    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:11.0.2.254  Bcast:0.0.0.0  Mask:255.255.255.0
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:25747 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:2008134 (1.9 MiB)

vlan12    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:111.0.254.254  Bcast:0.0.0.0  Mask:255.255.0.0
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:42 (42.0 B)

vlan13    Link encap:Ethernet  HWaddr 64:00:6a:f7:15:bd  
          inet addr:14.0.1.254  Bcast:0.0.0.0  Mask:255.255.255.0
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:42 (42.0 B)
"""
output_list = output.split('\n')
print(output_list)
i = 0
for line in output_list:
    if('Link' in line):
        print(line)
    if('errors' in line):
        match = re.search('errors:(\d+)', line)
        #print("Errors : %s" %match.group(1))
        print("Errors : {0}".format(match.group(1)))
        print(line)
        error_value = match.group(1)
        error_value_0 = match.group(0)
        print ("hello print group(1) : " + error_value)
        print("hello print group(0) : " + error_value_0)
        if int(error_value) < 10 :
            pass
        else :
            i+=1
if i > 0:
    print("Test Failed")
else:
    print("Test Passed")
