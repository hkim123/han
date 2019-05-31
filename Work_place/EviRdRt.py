'''
import os.path

def leaf01_tenant_virual_network(tenId,vniId,prefix):
    # Prompt the user to enter filename, Port scope mode
    f1 = input("Enter a filename: ").strip()

    if os.path.isfile(f1):
        print("The file already exists")
        return
    # Open files for output
    outfile = open(f1, "w")
    print(os.path.getmtime(f1))
    print("ip virtual-router mac-address 00:00:01:00:00:01",file = outfile)
    while tenId <= 32:
        # create Tenant
        print("", file=outfile)
        print("exit", file=outfile)
        print("ip vrf tenant0",tenId, sep='',file = outfile)
        print("", file=outfile)

        i = 1
        while i <= 4:
            # Create Virtual network
            print("virtual-network",vniId,file = outfile)
            print("member-interface ethernet 1/1/9 vlan-tag",vniId,file = outfile)
            print("member-interface ethernet 1/1/10 vlan-tag", vniId, file=outfile)
            print("member-interface port-channel 128 vlan-tag", vniId, file=outfile)
            print("vxlan-vni",vniId,file = outfile)
            print("",file = outfile)
            # Create Virtual network interface for ipv4 and ipv6
            print("interface virtual-network",vniId,file = outfile)
            print("ip vrf forwarding tenant0",tenId,sep='',file = outfile)
            print("ip address 192.168.",prefix,".1/24",sep ='',file = outfile)
            print("ip virtual-router address 192.168.",prefix,".254",sep='',file = outfile)
            print("ipv6 address 192:168:0:", prefix, "::1/64", sep='',file = outfile)
            print("ipv6 virtual-router address 192:168:0:", prefix, "::254", sep='',file = outfile)
            print("",file = outfile)

            i += 1
            vniId += 1
            prefix += 1
        tenId += 1


    outfile.close()

def leaf01_L2_virual_network():
    outfile1_L2 = open("leaf01_l2_vni.txt", "w")
    for l2Vni in range (2001,2873) :
        if l2Vni >= 2400:
            print("", file=outfile1_L2)
            print("virtual-network",l2Vni,file = outfile1_L2)
            print("member-interface ethernet 1/1/9 vlan-tag",l2Vni,file = outfile1_L2)
            print("member-interface ethernet 1/1/10 vlan-tag",l2Vni,file = outfile1_L2)
            print("member-interface port-channel 128 vlan-tag",l2Vni,file = outfile1_L2)
            print("vxlan-vni", l2Vni, file=outfile1_L2)
        else :
            print("", file=outfile1_L2)
            print("virtual-network", l2Vni, file=outfile1_L2)
            print("interface vlan", l2Vni, file=outfile1_L2)
            print("virtual-network", l2Vni, file=outfile1_L2)
            print("interface ethernet 1/1/9", file=outfile1_L2)
            print("switchport trunk allowed vlan ", l2Vni, file=outfile1_L2)
            print("interface ethernet 1/1/10", file=outfile1_L2)
            print("switchport trunk allowed vlan ", l2Vni, file=outfile1_L2)
            print("interface port-channel 128", file=outfile1_L2)
            print("switchport trunk allowed vlan ", l2Vni, file=outfile1_L2)

    outfile1_L2.close()

def leaf01_virtual_net_l2():
    outfile01_1 = open("leaf01_l2vni_attach.txt", "w")
    for vni in range (2001,2400):
        print("virtual-network",vni,file = outfile01_1)
        print("vxlan-vni",vni,file = outfile01_1)

    outfile01_1.close()



def leaf03_tenant_virual_network(tenId,vniId,prefix):
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    if os.path.isfile(f1):
        print("The file already exists")
        return
    # Open files for output
    outfile = open(f1, "w")
    print(os.path.getmtime(f1))
    print("ip virtual-router mac-address 00:00:01:00:00:01",file = outfile)
    while tenId <= 3:
        # create Tenant
        print("", file=outfile)
        print("ip vrf tenant0",tenId, sep='',file = outfile)
        print("", file=outfile)

        i = 1
        while i <= 4:
            # Create Virtual network
            print("virtual-network",vniId,file = outfile)
            print("member-interface ethernet 1/1/3 vlan-tag",vniId,file = outfile)
            print("member-interface ethernet 1/1/4 vlan-tag", vniId, file=outfile)
            print("vxlan-vni",vniId,file = outfile)
            print("",file = outfile)
            # Create Virtual network interface for ipv4 and ipv6
            print("interface virtual-network",vniId,file = outfile)
            print("ip vrf forwarding tenant0",tenId,sep='',file = outfile)
            print("ip address 192.168.",prefix,".3/24",sep ='',file = outfile)
            print("ip virtual-router address 192.168.",prefix,".254",sep='',file = outfile)
            print("ipv6 address 192:168:0:", prefix, "::3/64", sep='',file = outfile)  ### consider above hex increament
            print("ipv6 virtual-router address 192:168:0:", prefix, "::254", sep='',file = outfile)
            print("",file = outfile)

            i += 1
            vniId += 1
            prefix += 1
        tenId += 1


    outfile.close()

def leaf04_tenant_virual_network(tenId,vniId,prefix):
    ## port based mode ###
    outfile4 = open("leaf04_tenant_vni_interface.txt", "w")
#    print(os.path.getmtime(outfile5.strip()))
    print("ip virtual-router mac-address 00:00:01:00:00:01",file = outfile4)
#    print("interface ethernet 1/1/3:1", file=outfile4)
#    print("switchport mode trunk", file=outfile4)
#    print("no switchport access vlan ", file=outfile4)
#    print("interface ethernet 1/1/4:1", file=outfile4)
#    print("switchport mode trunk", file=outfile4)
#    print("no switchport access vlan ", file=outfile4)
#    vlanId = 3001
#    ip = 31
    while tenId <= 32:
        # create Tenant
        print("exit", file=outfile4)
        print("ip vrf tenant0",tenId, sep='',file = outfile4)
#        print("interface vlan ",vlanId,file = outfile4)
#        print("ip vrf forwarding tenant0", tenId,sep='',file = outfile4)
#        print("ip address 131.31.",ip,".1/24",sep ='',file = outfile4)
        print("", file=outfile4)

        i = 1
        while i <= 4:
            # Create Virtual network
            print("virtual-network",vniId,file = outfile4)
            print("vxlan-vni",vniId,file = outfile4)
            print("",file = outfile4)
            print("interface vlan ", vniId, file=outfile4)
            print("virtual-network ", vniId, file=outfile4)
            # Create Virtual network interface for ipv4 and ipv6
            print("interface virtual-network",vniId,file = outfile4)
            print("ip vrf forwarding tenant0",tenId,sep='',file = outfile4)
            print("ip address 192.168.",prefix,".4/24",sep ='',file = outfile4)
            print("ip virtual-router address 192.168.",prefix,".254",sep='',file = outfile4)
            print("ipv6 address 192:168:0:", prefix, "::4/64", sep='',file = outfile4)
            print("ipv6 virtual-router address 192:168:0:", prefix, "::254", sep='',file = outfile4)
            print("interface ethernet 1/1/3:1", file=outfile4)
            print("switchport trunk allowed vlan ", vniId, file=outfile4)
            print("interface ethernet 1/1/4:1", file=outfile4)
            print("switchport trunk allowed vlan ", vniId, file=outfile4)
            print("",file = outfile4)

            i += 1
            vniId += 1
            prefix += 1

        tenId += 1
#        vlanId += 1
#        ip += 1

    outfile4.close()

def leaf04_L2_virual_network():
    outfile4_L2 = open("leaf04_l2_vni.txt", "w")
    for l2Vni in range (2001,2873) :
        if l2Vni <= 2400:
            print("", file=outfile4_L2)
            print("virtual-network",l2Vni,file = outfile4_L2)
            print("member-interface ethernet 1/1/3:1 vlan-tag",l2Vni,file = outfile4_L2)
            print("member-interface ethernet 1/1/4:1 vlan-tag",l2Vni,file = outfile4_L2)
            print("vxlan-vni", l2Vni, file=outfile4_L2)
        else :
            print("", file=outfile4_L2)
            print("virtual-network", l2Vni, file=outfile4_L2)
            print("interface vlan", l2Vni, file=outfile4_L2)
            print("virtual-network", l2Vni, file=outfile4_L2)
            print("interface ethernet 1/1/3:1", file=outfile4_L2)
            print("switchport trunk allowed vlan ", l2Vni, file=outfile4_L2)
            print("interface ethernet 1/1/4:1", file=outfile4_L2)
            print("switchport trunk allowed vlan ", l2Vni, file=outfile4_L2)



    print("evpn", file=outfile4_L2)

    rt = 16779217
    for evi in range (2001,2873) :
        print("",file=outfile4_L2)
        print("evi", evi, file=outfile4_L2)
        print("vni", evi, file=outfile4_L2)
        print("rd 9.9.9.9:",evi,sep='', file=outfile4_L2)
        print("route-target 65500:",rt," both",sep='', file=outfile4_L2)

        rt += 1


    outfile4_L2.close()



def leaf04_evi_rd_rt(evi,netID04):
    outfile04 = open("leaf04_evi_rd_rt.txt", "w")
    print("evpn", file=outfile04)

    while evi <= 1128 :
        if evi <= 1064:  #both rd and RT are manual
            print("",file = outfile04)
            print("evi",evi,file = outfile04)
            print("vni",evi,file = outfile04)
            print("rd 4.4.4.4:",evi,sep='',file = outfile04)
            print("route-target 65500:",netID04," both",sep='',file = outfile04)
            netID04 += 1

        else:  #rd is auto, rt is auto
            print("", file=outfile04)
            print("evi", evi,file = outfile04)
            print("vni", evi,file = outfile04)
            print("rd auto",file = outfile04)
            print("route-target auto", file=outfile04)



        evi += 1


    outfile04.close()

def leaf04_virtual_net_l2():
    outfile04_1 = open("leaf04_l2vni_attach.txt", "w")
    for vni in range (2401,2873):
        print("virtual-network",vni,file = outfile04_1)
        print("vxlan-vni",vni,file = outfile04_1)

    outfile04_1.close()



def leaf05_tenant_virual_network(tenId,vniId,prefix):
    ## vlan attached mode for L3 vni ###
    outfile5 = open("leaf05_tenant_vni_interface.txt", "w")
#    print(os.path.getmtime(outfile5.strip()))
    print("ip virtual-router mac-address 00:00:01:00:00:01",file = outfile5)
    while tenId <= 32:
        # create Tenant
        print("exit", file=outfile5)
        print("ip vrf tenant0",tenId, sep='',file = outfile5)
        print("", file=outfile5)

        i = 1
        while i <= 4:
            # Create Virtual network
            print("virtual-network",vniId,file = outfile5)
            print("vxlan-vni",vniId,file = outfile5)
            print("",file = outfile5)
            print("interface vlan ",vniId,file = outfile5)
            print("virtual-network ",vniId,file = outfile5)
            # Create Virtual network interface for ipv4 and ipv6
            print("interface virtual-network",vniId,file = outfile5)
            print("ip vrf forwarding tenant0",tenId,sep='',file = outfile5)
            print("ip address 192.168.",prefix,".5/24",sep ='',file = outfile5)
            print("ip virtual-router address 192.168.",prefix,".254",sep='',file = outfile5)
            print("ipv6 address 192:168:0:", prefix, "::5/64", sep='',file = outfile5)
            print("ipv6 virtual-router address 192:168:0:", prefix, "::254", sep='',file = outfile5)
            print("interface ethernet 1/1/1",file=outfile5)
            print("switchport trunk allowed vlan ",vniId, file=outfile5)
            print("interface ethernet 1/1/2", file=outfile5)
            print("switchport trunk allowed vlan ", vniId, file=outfile5)
            print("",file = outfile5)

            i += 1
            vniId += 1
            prefix += 1
        tenId += 1


    outfile5.close()

def leaf05_L2_virual_network():
    outfile5_L2 = open("leaf05_l2_vni.txt", "w")
    for l2Vni in range (2001,2873) :
        print("", file=outfile5_L2)
        print("virtual-network",l2Vni,file = outfile5_L2)
        print("member-interface ethernet 1/1/1 vlan-tag",l2Vni,file = outfile5_L2)
        print("member-interface ethernet 1/1/2 vlan-tag",l2Vni,file = outfile5_L2)
        print("vxlan-vni", l2Vni, file=outfile5_L2)

    print("evpn", file=outfile5_L2)
    for evi in range (2001,2873) :
        print("",file=outfile5_L2)
        print("evi", evi, file=outfile5_L2)
        print("vni", evi, file=outfile5_L2)
        print("rd auto", file=outfile5_L2)
        print("route-target auto", file=outfile5_L2)

    outfile5_L2.close()

def leaf05_evi_rd_rt(evi,netID05):
    outfile05 = open("leaf05_evi_rd_rt.txt", "w")
    print("evpn", file=outfile05)

    while evi <= 1128 :
        if evi <= 1032:  #both rd and RT are auto
            print("",file = outfile05)
            print("evi",evi,file = outfile05)
            print("vni",evi,file = outfile05)
            print("rd auto",file = outfile05)
            print("route-target auto",file = outfile05)

        elif evi <= 1064:  #rd is manual, rt is auto
            print("", file=outfile05)
            print("evi", evi,file = outfile05)
            print("vni", evi,file = outfile05)
            print("rd 5.5.5.5:",evi,sep='',file = outfile05)
            print("route-target auto",file = outfile05)

        elif evi <= 1097:  #rd is auto, rt is manual
#            netID05 = 16778281
            print("", file=outfile05)
            print("evi", evi,file = outfile05)
            print("vni", evi,file = outfile05)
            print("rd auto",file = outfile05)
            print("route-target 65500:",netID05," both",sep='',file = outfile05)
            netID05 += 1
        else:
#            netID05 = 16778313 #rd and rt are manual
            print("", file=outfile05)
            print("evi", evi, file=outfile05)
            print("vni", evi, file=outfile05)
            print("rd 6.6.6.6:",evi, sep='', file=outfile05)
            print("route-target 65500:",netID05," both",sep='',file=outfile05)
            netID05 += 1

        evi += 1


    outfile05.close()


def border_tenant_virual_network_1(tenId,vniId,prefix):
    outfile3 = open("border_tenant_vni_interface.txt", "w")
    print("ip virtual-router mac-address 00:00:01:00:00:02",file = outfile3)
    while tenId <= 16:
        # create Tenant
        print("", file=outfile3)
        print("exit", file=outfile3)  ################################# First exit require remove otherwise error ######
        print("ip vrf tenant0",tenId, sep='',file = outfile3)
        print("", file=outfile3)

        i = 1
        while i <= 4:
            # Create Virtual network
            print("virtual-network",vniId,file = outfile3)
            print("vxlan-vni",vniId,file = outfile3)
            print("",file = outfile3)
            # Create Virtual network interface for ipv4 and ipv6
            print("interface virtual-network",vniId,file = outfile3)
            print("ip vrf forwarding tenant0",tenId,sep='',file = outfile3)
            print("ip address 192.168.",prefix,".3/24",sep ='',file = outfile3)
            print("ip virtual-router address 192.168.",prefix,".253",sep='',file = outfile3)
            print("ipv6 address 192:168:0:", prefix, "::3/64", sep='',file = outfile3)
            print("ipv6 virtual-router address 192:168:0:", prefix, "::253", sep='',file = outfile3)

            print("",file = outfile3)

            i += 1
            vniId += 1
            prefix += 1
        tenId += 1

    prefix_1 = 1
    for vlan in range(3001,3017):
        print("exit", file=outfile3)
        print("interface vlan", vlan, file=outfile3)
        print("ip vrf forwarding tenant0", prefix_1, sep='', file=outfile3)   ### require this command before ip address #####
        print("ip address 200.1.", prefix_1, ".254/24", sep='', file=outfile3)
        prefix_1 += 1

    outfile3.close()


def border_tenant_virual_network_2(tenId,vniId,prefix):
    outfile3_1 = open("border_tenant_vni_vrf_extent.txt", "w")

    for tenantID in range(17,33):
        print("", file=outfile3_1)
        print("exit",file=outfile3_1)  ################################# First exit require remove otherwise error ######
        print("ip vrf tenant0", tenantID, sep='', file=outfile3_1)
        print("", file=outfile3_1)

        for i in range(1,5):
            # Create Virtual network
            print("virtual-network", vniId, file=outfile3_1)
            print("member-interface ethernet 1/1/42 vlan-tag", vniId, file=outfile3_1)
            print("vxlan-vni", vniId, file=outfile3_1)
            print("", file=outfile3_1)
            # Create Virtual network interface for ipv4 and ipv6
            print("interface virtual-network", vniId, file=outfile3_1)
            print("ip vrf forwarding tenant0", tenId, sep='', file=outfile3_1)
            print("ip address 192.168.", prefix, ".3/24", sep='', file=outfile3_1)
            print("ip virtual-router address 192.168.", prefix, ".253", sep='', file=outfile3_1)
            print("ipv6 address 192:168:0:", prefix, "::3/64", sep='', file=outfile3_1)
            print("ipv6 virtual-router address 192:168:0:", prefix, "::253", sep='', file=outfile3_1)

            print("", file=outfile3_1)

            vniId += 1
            prefix += 1
        tenId += 1


    outfile3_1.close()



def tor_02_vrf_extend():
    outfile7 = open("tor_02_vrf_vlan.txt", "w")
    toR2_vni = 1065
    for tenant in range (17,25):
        print("", file=outfile7)
        print("exit",file=outfile7)  ################################# First exit require remove otherwise error ######
        print("ip vrf tenant0", tenant, sep='', file=outfile7)
        print("", file=outfile7)
        print("exit", file=outfile7)
        print("interface vlan", toR2_vni, file=outfile7)
        print("ip vrf forwarding tenant0", tenant, sep='', file=outfile7)
        toR2_vni += 4


    outfile7.close()

def delete_ipv6():
    outfile_del = open("ipv6_del.txt","w")
    i = 1
    for vni in range(1001,1129):
        print("interface virtual-network", vni,file=outfile_del)
        print("no ipv6 address 192:168:0:",i,"::4/64",sep='',file=outfile_del)
        i += 1


def leaf01_hex_increase():
    outfile1_l3_hex = open("leaf03_hex_ip.txt", "w")
    v6 = 1
    for vn_net in range(1001,1129):
        print ("interface virtual-network",vn_net,file = outfile1_l3_hex)
        print ("ipv6 address 192:168:0:",hex(v6)[2:],"::4/64",sep='',file = outfile1_l3_hex)
        print("ipv6 virtual-router address 192:168:0:",hex(v6)[2:], "::254", sep='',file = outfile1_l3_hex)
        print('')
        v6 += 1
#        print(hex(i)[2:])
    outfile1_l3_hex.close()

def ipv4():
    i = 1
    for vn_net in range(1001,1129):
        print("interface virtual-network", vn_net)
        print("ip address 192.168.",i,".2/24",sep='')
        i += 1

def main():
    tenantId = 1
    vniId = 1001
    ip_prefix = 1
#    leaf01_tenant_virual_network(tenantId, vniId, ip_prefix)
#    leaf04_tenant_virual_network(tenantId, vniId, ip_prefix)
#    leaf04_evi_rd_rt(1001, 16778217)
#    leaf05_tenant_virual_network(tenantId, vniId, ip_prefix)
#    leaf05_evi_rd_rt(1001,16778281)
#    leaf05_L2_virual_network()
#    leaf04_L2_virual_network()
#    leaf01_L2_virual_network()
#    border_tenant_virual_network_1(tenantId, vniId, ip_prefix)
#    border_tenant_virual_network_2(17, 1065, 65)
#    tor_02_vrf_extend()
#    leaf04_virtual_net_l2()
#    leaf01_virtual_net_l2()
#    leaf01_hex_increase()
#    delete_ipv6()
    ipv4()
main()
'''
'''
vni = 3001
#rd = 1001
rt = 268438457
for evi in range(1001,2001) :
    print('!')
    print('evi',evi)
    print('vni',vni)
#    print('rd 55.55.55.55:',rd,sep='')
    print('rd auto')
    print('route-target ','65534:',rt,' both',sep='')
    vni = vni + 1
#    rd = rd + 1
    rt = rt + 1
'''
'''
j = 1
for i in range(1001,1005):
    print("!")
    print('interface virtual-network',i)
    print('ip address',' 10.',j,'.0.3/16',sep='')
    print('ip virtual-router address',' 10.',j,'.255.253',sep='')
    print('ipv6 address',' 10:',j,'::3/64',sep='')
    print('ipv6 virtual-router address',' 10:',j,'::ffff:0:0:2',sep='')
    j = j + 1
'''
j = 1
for i in range (4001,4032):
    print("!")
    print('interface vlan',i)
    print('ip vrf forwarding vrf_',j,sep='')
    print('ip address 200.1.',j,'.253/24',sep='')
    j = j +1