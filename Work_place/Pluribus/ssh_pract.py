#! /usr/local/bin/python3
#Popen usage
#p = Popen(arg,stdin = PIPE,stdout = PIPE,stderr = PIPE)

#from subprocess import PIPE, Popen
import subprocess
import shlex

cmd = 'cli vrouter-show name leopst1'
#cmd = 'pkg info pn-nvos'
cmd_1 = 'cli bootenv-show'
#stream = Popen(['ssh','root@leo-pst-1',cmd],stdin=PIPE, stdout=PIPE)
#rsp = stream.stdout.read().decode('utf-8')
#print(rsp)
#sp_pkg = subprocess.Popen(['ssh','root@leo-pst-1',cmd],stdin=PIPE, stdout=PIPE)
#sp_boot = subprocess.Popen




ps = subprocess.Popen(['ssh','root@leo-pst-1',cmd_1],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = ps.stdout.read().decode('utf-8')

#output = ps.communicate()[0]
print(output)

#output_1 = Popen(['ssh','root@leo-pst-1',cmd_1],stdin=output.stdout, stdout=PIPE)
#resp_1 = output_1.stdout.read().decode('utf-8')

#print(resp_1)
