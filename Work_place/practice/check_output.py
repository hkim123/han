#!/usr/bin/python
from subprocess import *

out = check_output('ls' , shell=True)
print out
p = Popen('pwd', shell=True, stdout=PIPE)
(out, err) = p.communicate()

print out
print err


