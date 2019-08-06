#!/usr/bin/python
from __future__ import print_function
import pexpect


### Variable ###
ToR_2 = '10.11.138.5'
ToR_1 = '10.11.138.6'


user = 'admin'
password = 'admin'

#PROMPT = ['~# ','# ', '>>> ', '> ', '\$ ', 'admin: ']
PROMPT = ['~# ','# ', '\$ ', 'admin: ']

def send_cmd(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before + child.after, end='')


def ssh_conn(user, host, password):
    ssh_key = 'Are you sure you want to continue connecting'
    ssh_host = '%s@%s' % (user, host)
    child = pexpect.spawn('ssh ' + ssh_host)

#    ret = child.expect([pexpect.TIMEOUT, ssh_key, "%s's password:" % ssh_host])

#    if ret == 0:
#            print '[-] Error Connecting'
#            exit(0)
#    if ret == 1:
#            child.sendline('yes')
#            ret = child.expect([pexpect.TIMEOUT, "%s's password:" % ssh_host])
#            if ret == 0:
#                    print '[-] Error Connecting'
#                    exit(0)

    child.expect('password: ')    
    child.sendline(password)
    child.expect(PROMPT)
    print(child.before + child.after, end='')
    return child


def main():

    child = ssh_conn(user, ToR_2, password)
    send_cmd(child, 'show version')
    send_cmd(child, 'show boot')

#   Go to Kernel
    send_cmd(child, 'system ''"''sudo -i')
    send_cmd(child, 'admin')

#   check interface
    send_cmd(child, 'ifconfig -a')
    raw_input("Press Enter to continue...")

# Port Mapping
    send_cmd(child, 'python /opt/dell/os10/bin/dn_portmap.py')
    send_cmd(child, 'hshell -c ''"''ps''"')
    raw_input("Press Enter to continue...")

# MAC address
    #send_cmd(child, 'bridge fdb')  #Kernel command
    #send_cmd(child, 'hshell -c ''"''l2 show''"')  #Hardware command
    #send_cmd(child, '\n')
    #raw_input("Press Enter to continue...")

# Spanning Tress
    #send_cmd(child, 'brctl show stp br1')
    #send_cmd(child, 'brctl showstp br1')
    #send_cmd(child, 'hshell -c ''"''stg show''"')
    #send_cmd(child, '\n')
    #raw_input("Press Enter to continue...")

#    send_cmd(child,'config t')
#    send_cmd(child,'do show vlan | no-more')
#    send_cmd(child, 'show version')


    host_2 = '10.11.138.6'
    child_2 = ssh_conn(user, ToR_1, password)
    send_cmd(child_2, 'show version')
    send_cmd(child_2, 'show boot')

if __name__ == '__main__':
    main()

