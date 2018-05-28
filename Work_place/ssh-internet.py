#!/usr/bin/python

import pexpect
PROMPT = ['~# ','# ', '>>> ', '> ', '\$ ']


def send_cmd(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before


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

#    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = '10.11.131.37'
    user = 'root'
    password = 'root'
    child = ssh_conn(user, host, password)
    send_cmd(child, 'uname -v')
    send_cmd(child, 'ifconfig eth0')

if __name__ == '__main__':
    main()
