#! /usr/local/bin/python3
#Popen usage 
#p = Popen(arg,stdin = PIPE,stdout = PIPE,stderr = PIPE)

from subprocess import PIPE, Popen

cmd = 'pkg info pn-nvos'
cmd_1 = 'cli bootenv-show'
#stream = Popen(['ssh','root@leo-pst-1',cmd],stdin=PIPE, stdout=PIPE)
#rsp = stream.stdout.read().decode('utf-8')
#print(rsp)
output = Popen(['ssh','root@leo-pst-1',cmd],stdin=PIPE, stdout=PIPE)
resp = output.stdout.read().decode('utf-8')

print(resp)

output_1 = Popen(['ssh','root@leo-pst-1',cmd_1],stdin=PIPE, stdout=PIPE)
resp_1 = output_1.stdout.read().decode('utf-8')

print(resp_1) 
