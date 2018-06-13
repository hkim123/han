import re

output = """top - 17:58:20 up 7 days, 18:47,  2 users,  load average: 0.08, 0.13, 0.15 
Tasks: 125 total,   1 running, 124 sleeping,   0 stopped,   0 zombie 
%Cpu(s):  1.7 us,  3.0 sy,  0.4 ni, 94.8 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem:   8180604 total,  3213868 used,  4966736 free,   145804 buffers
KiB Swap:        0 total,        0 used,        0 free.  2119560 cached Mem """

if "KiB Mem" in output:
    match=re.search('KiB Mem:\s+([0-9]+) total,\s+([0-9]+) used,\s+([0-9]+) free,',  output)
    if match:
        mem_threshold = int(match.group(3)) / int(match.group(1))*100
        print (mem_threshold)
        if(mem_threshold > 30) :
            print("pass: memory Usage: %s %s %s"%(match.group(1),match.group(2),match.group(3)))
        else :
            print ("test fail memory is too high")
    else:
        print("testFailed... Could not find memory output")
else:
    print("testFailed... Error in executing memory usage for top command")
