#!/usr/bin/python
#This is working one
import pexpect
PROMPT = ['~# ','# ', '>>> ', '> ', '\$ ']


def send_cmd(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before
    print child.after

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
    return child


def main():
    host = '10.11.131.44'
    user = 'root'
    password = 'root'
    child = ssh_conn(user, host, password)
#    send_cmd(child, 'lldpctl')
    send_cmd(child, 'ifconfig -a')

if __name__ == '__main__':
    main()
