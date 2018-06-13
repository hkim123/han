#!/usr/bin/python
from subprocess import Popen
from subprocess import PIPE

def get_cmd(args):
    cmd = 'cat ' + args
    p = Popen(cmd, shell=True, stdout=PIPE)
    (ret, err) = p.communicate()
    return ret

if __name__ == "__main__" :
  args = 'message.log' 
  
  print get_cmd(args)
   
