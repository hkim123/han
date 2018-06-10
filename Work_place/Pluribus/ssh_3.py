#! /usr/bin/env/python3

import paramiko

ip='leo-pst-1'
port=22
username='root'
password='test123'

cmd='df' 

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

print ("check software version\n")

stdin,stdout,stderr=ssh.exec_command('pkg info pn-nvos')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
