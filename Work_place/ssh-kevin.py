#! /usr/bin/python

import pexpect
import re
from time import sleep
from datetime import datetime
import socket
import sys
import os


#### SSH example

def main():
    # Server on which sim will be spawned
    server = '10.11.131.37'

    # Username and password for users with permissions to launch and also apply ssh port forwarding (if using port forwarding)
    username = 'root'
    password = 'root'

    print("Connecting to quagga device {} ".format(server))
    proc = pexpect.spawn('ssh -o CheckHostIP=no -o StrictHostKeyChecking=no {}@{}'.format(username, server))
    proc.logfile = sys.stdout
    log.info(proc.after)
#    proc.logfile = os.fdopen (sys.stdout.fileno(),"w",0)
#    sys.stdout = open ("ssh_result.txt","w")
#    proc.expect(['password:'], timeout=10)
#    proc.sendline(password)
#    proc.expect(r'.*[\$#]', timeout=10)
    proc.expect(r'.*[~#]', timeout=10)

    proc.sendline('ifconfig eth0')
#    proc.sendline('ps aux | grep ssh')
#    sys.stdout.write = output
#    print proc.before
#    proc.logfile = sys.stdout
#    output = proc.before
#    print output
#    proc.expect([r'.*[~#]'], timeout=60)
#    proc.expect(r'.*[~#]', timeout=10)
#    print proc.sendline()
#    proc.sendline()
    proc.expect(r'.*[~#]', timeout=10)
    proc.close(); sleep(10)



if __name__ == '__main__':
    main()

##### telnet multiple devices example
#
#def main():
#
#    # router hostname, console ports, ip to assign to eth-mgmt of each router, and ssh port to use for redirecting to the ips
#    con_ports = ['7001', '7011']
#    ips = ['192.168.122.70', '192.168.122.71']
#
#    server = '10.195.122.233'
#
#    for address, port in zip(ips, con_ports):
#
#        proc = pexpect.spawn("telnet {} {}".format(server, port))
#        proc.sendline()
#        proc.sendline()
#        proc.expect([r'xr login:'], timeout=1800); sleep(60)
#        proc.sendline()
#        proc.sendline()
#
#        print("Entering linux username 'root' and password 'lab'")
#        proc.sendline('root')
#        proc.expect([r'New password:'], timeout=10)
#        proc.sendline('lab')
#        proc.expect([r'Retype new password:'], timeout=10)
#        proc.sendline('lab')
#        proc.expect([r"root@xr:~#"], timeout=60)
#        print("Reached linux prompt, CURRENT PROMPT: {}".format(proc.match.group().decode()))
#        proc.close()


#if __name__ == '__main__':
#    main()
