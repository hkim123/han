#!/usr/bin/python
import os

OS_1 = os.system("uname -a|grep SunOS")
OS_2 = os.system("uname -a|grep Linux")

def check():
    datafile = file('/etc/ssh/sshd_config')
    found = False
    for line in datafile:
        if 'PermitRootLogin yes' in line:
           found = True
           break

    return found
found = check ()

if found:
    print "Already set to yes"
else:
    print "Need to set it"

os.system("perl -pi -e 's/^.?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config")

if (OS_1 == 0):
    os.system("rolemod -K type=normal root")
    os.system ("passwd root")
    os.system("svcadm restart ssh")

elif (OS_2 == 0):
    os.system ("passwd root")
    os.system ("service ssh restart")
else:
    print "Platform is neither Linux nor SunOS"
