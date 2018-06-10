#!/usr/bin/python
#monitoring log shows alarm when search string (err or fail) find
#add color when alert happen
from faillog_recent import get_log_data
from time import sleep
import os
import sys
import datetime


#color
errcolor_fatal= '\033[31m'
errcolor_none = '\033[0m'
errcolor_except = '\x1b[36m'

def check(file_name, search_word, out_file_name) :
    if os.path.exists(file_name):
        print "start monitoring: ", file_name
        print "search : ", search_word
        print "-" * 70
    else :
        print "No file : ", file_name

    index = 0
    while os.path.exists(file_name) :
        fp = open(file_name)
        file_data = fp.read()
        index = file_data.find(search_word, index)
        fp.close()

        if  index >=0 :
            alert(search_word)
            (data,count) = get_log_data(file_data, search_word, index, 2, 2)
            
            out_file = open(out_file_name, "a")
	    out_file.write("\n" + ("*" * 70) )
            out_file.write("\n start time when happen ("+search_word+"): " )
            out_file.write(str(datetime.datetime.now()))
            out_file.write("\n" + ("-" * 70) + "\n")
            out_file.write(data)
	    print "Please take a look log file: ", out_file_name
            out_file.close()
        else :
            sys.stdout.write(".....")
            sys.stdout.flush()

        index = len(file_data)
        sleep(5)
def alert(search_word) :
    now = datetime.datetime.now()
    if search_word == "FATAL" :
        print errcolor_fatal + "\n", now, "Alert ERROR !!!!" +errcolor_none
    elif search_word == "except" :

        print errcolor_except +"\n", now, "ERROR ERROR !!!!!!" +errcolor_none

if __name__ == "__main__":
    check("/var/log/syslog", "FATAL", "/var/log/fatal_log")
