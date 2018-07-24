#!/usr/bin/python
#find fail from the log and display before and after lines, it works with mylog.py 
import mylog
mylog.printlog("/var/log/system.log", "fail", 3, 5)
