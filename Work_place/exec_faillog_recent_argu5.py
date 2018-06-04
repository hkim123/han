#!/usr/bin/python
#find fail from the log and display before and after lines but it start look at from half to end.

import faillog_recent
import os
logfile = "/var/log/system.log"
file_length = os.path.getsize(logfile)
print file_length
faillog_recent.printlog("/var/log/system.log", "err", int(file_length/2), 3, 5)
