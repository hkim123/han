#!/usr/bin/python
#find fail from the log and display before and after lines.
#it will find all fails in the logs
import faillog
faillog.printlog("/var/log/system.log", "err", 3, 5)
