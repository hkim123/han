import sys
l3vlan1 = range (1001, 1033)
l3vlan2 = ['4094']
l2vlan1 = range(3001, 3017)
l2vlan2 = range(3501, 3517)
bond1 = ['11']
bond1_int =['e101-001-1', 'e101-001-2', 'e101-001-3', 'e101-001-4', 'e101-002-1', 'e101-002-2', 'e101-002-3', 'e101-002-4', 'e101-003-1', 'e101-003-2', 'e101-003-3', 'e101-003-4', 'e101-004-1', 'e101-004-2', 'e101-004-3', 'e101-004-4']
bond2 = ['127', '128', '31', '32', '41', '42']
bond2_int1 = ['e101-009-1', 'e101-009-2', 'e101-009-3', 'e101-009-4', 'e101-010-1', 'e101-010-2']
bond2_int2 = ['e101-010-3', 'e101-010-4', 'e101-011-1', 'e101-011-2', 'e101-011-3', 'e101-011-4']
bond2_int3 = ['e101-017-1', 'e101-017-2', 'e101-017-3', 'e101-017-4']
bond2_int4 = ['e101-018-1', 'e101-018-2', 'e101-018-3', 'e101-018-4']
bond2_int5 = ['e101-019-1', 'e101-019-2', 'e101-019-3', 'e101-019-4']
bond2_int6 = ['e101-020-1', 'e101-020-2', 'e101-020-3', 'e101-020-4']
bond2_ports = [bond2_int1, bond2_int2, bond2_int3, bond2_int4, bond2_int5, bond2_int6]
file=open('/etc/network/interfaces', 'a')
x = 0
y = 100
z = 150
for bid, port in zip(bond2, bond2_ports):
        file.write("auto bond%s"%bid)
        file.write("\n")
        file.write("iface bond%s inet manual"%bid)
        file.write("\n")
        file.write("up ifconfig bond%s 0.0.0.0 up"%bid)
        file.write("\n")
        file.write("bond-slaves %s"%(' '.join(str(p) for p in port)))
        file.write("\n")
        file.write("bond-mode 802.3ad")
        file.write("\n")
        file.write("bond-miimon 100")
        file.write("\n")
        file.write("bond-lacp-rate 1")
        file.write("\n")
        file.write("bond-min-links 1")
        file.write("\n")
        for vid in l2vlan1:
                file.write("auto bond%s.%s"%(bid, str(vid)))
                file.write("\n")
                file.write("iface bond%s.%s inet manual"%(bid, str(vid)))
                file.write("\n")
        for vid in l2vlan2:
                file.write("auto bond%s.%s"%(bid, str(vid)))
                file.write("\n")
                file.write("iface bond%s.%s inet manual"%(bid, str(vid)))
                file.write("\n")
        for  vid in l3vlan2:
                file.write("auto bond%s.%s"%(bid, vid))
                file.write("\n")
                file.write("iface bond%s.%s inet manual"%(bid, vid))
                file.write("\n")
for bid in bond1:
        file.write("auto bond%s"%bid)
        file.write("\n")
        file.write("iface bond%s inet manual"%bid)
        file.write("\n")
        file.write("up ifconfig bond%s 0.0.0.0 up"%bid)
        file.write("\n")
        file.write("bond-slaves %s"%(' '.join(str(p) for p in bond1_int)))
        file.write("\n")
        file.write("bond-mode 802.3ad")
        file.write("\n")
        file.write("bond-miimon 100")
        file.write("\n")
        file.write("bond-lacp-rate 1")
        file.write("\n")
        file.write("bond-min-links 1")
        file.write("\n")
        for vid in l3vlan1:
                file.write("auto bond%s.%s"%(bid, str(vid)))
                file.write("\n")
                file.write("iface bond%s.%s inet manual"%(bid, str(vid)))
                file.write("\n")
for vid in l2vlan1:
        y += 1
        ipv4 = "100.%s.0.2/16"%y
        file.write("auto br%s"%str(vid))
        file.write("\n")
        file.write("iface br%s inet static"%str(vid))
        file.write("\n")
        file.write("address %s"%ipv4)
        file.write("\n")
        file.write("bridge-ports bond{1}.{0} bond{2}.{0} bond{3}.{0} bond{4}.{0} bond{5}.{0} bond{6}.{0}".format(str(vid), bond2[0], bond2[1], bond2[2], bond2[3], bond2[4], bond2[5]))
        file.write("\n")
        file.write ("bridge-stp on")
        file.write("\n")
        file.write ("bridge-bridgeprio 8192")
        file.write("\n")
for vid in l2vlan2:
        z += 1
        ipv4 = "100.%s.0.2/16"%z
        file.write("auto br%s"%str(vid))
        file.write("\n")
        file.write("iface br%s inet static"%str(vid))
        file.write("\n")
        file.write("address %s"%ipv4)
        file.write("\n")
        file.write("bridge-ports bond{1}.{0} bond{2}.{0} bond{3}.{0} bond{4}.{0} bond{5}.{0} bond{6}.{0}".format(str(vid), bond2[0], bond2[1], bond2[2], bond2[3], bond2[4], bond2[5]))
        file.write("\n")
        file.write ("bridge-stp on")
        file.write("\n")
        file.write ("bridge-bridgeprio 16384")
        file.write("\n")
file.write("auto br%s"%l3vlan2[0])
file.write("\n")
file.write("iface br%s inet static"%l3vlan2[0])
file.write("\n")
file.write("address 100.3.1.1/16")
file.write("\n")
file.write("bridge-ports bond{1}.{0} bond{2}.{0} bond{3}.{0} bond{4}.{0} bond{5}.{0} bond{6}.{0}".format(l3vlan2[0], bond2[0], bond2[1], bond2[2], bond2[3], bond2[4], bond2[5]))
file.write("\n")
file.write ("bridge-stp on")
file.write("\n")
for vid in l3vlan1:
        x += 1
        ipv4 = "100.1.%s.2/24"%x
        file.write("auto br%s"%str(vid))
        file.write("\n")
        file.write("iface br%s inet static"%str(vid))
        file.write("\n")
        file.write("address %s"%ipv4)
        file.write("\n")
        file.write("bridge-ports bond{1}.{0}".format(str(vid), bond1[0]))
        file.write("\n")
file.close()
