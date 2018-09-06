#!/usr/bin/python
#monitoring log shows alarm when search string (err or fail) find
from faillog_recent import get_log_data
from time import sleep
import os
import sys
import datetime

def check(file_name, search_word) :
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

        if index >=0 :
            alert()
            (data,count) = get_log_data(file_data, search_word, index, 2, 2)
            print data
        else :
            sys.stdout.write(".....")
            sys.stdout.flush()
            index = len(file_data)
            sleep(5)

def alert() :
    print "\n", datetime.datetime.now(), "ERROR ERROR !!!!!!"

if __name__ == "__main__":
    check("/var/log/syslog", "han")

