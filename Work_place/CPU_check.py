import re
max_cpu = 50

#output = open('top.txt')
#print (output.read())


output = """top - 17:58:20 up 7 days, 18:47,  2 users,  load average: 0.08, 0.13, 0.15 
Tasks: 125 total,   1 running, 124 sleeping,   0 stopped,   0 zombie 
%Cpu(s):  1.7 us,  3.0 sy,  0.4 ni, 94.8 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem:   8180604 total,  3213868 used,  4966736 free,   145804 buffers
KiB Swap:        0 total,        0 used,        0 free.  2119560 cached Mem """


if "Cpu" in output:
    #match = re.search('Cpu.* ([0-9]+.[0-9]+) id', output)  # need figure out why shows up all value, I thought only last 2, it figured out. below works
    match = re.search('Cpu.* ([0-9].*) id', output)
    print (match)
    print (match.group(1))
    if match:
        cpu = 100 - float(match.group(1))
        if (cpu < max_cpu):
             print("CPU Usage: %s is with in the max_cpu threshold" % cpu)
        else:
             print("testFailed, CPU usage is more than the max_cpu threshold defined. It is at %s" % cpu)
    else:
         print("Test Failed, Could not find idle CPU")
else:
     print("Test Failed, Error in executing CPU usage top command")

#output.close()