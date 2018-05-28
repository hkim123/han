#!/usr/bin/python

def printlog(logfile, search_word):
    f = open(logfile)
    logdata = f.read()
    f.close

    index = logdata.find(search_word)
    if index >= 0 :

        print "-" * 70
        print "Log file: " , logfile
        print "Find this word: ", search_word
        print index
        print "-" * 70

        print get_log_data(logdata,index)
        print "-" * 70

def get_log_data(logdata,start_index) :
    enter_index = max(0,logdata.rfind("\n", 0, start_index ))
    enter_index2 = logdata.find("\n", start_index, len(logdata))
    return logdata[enter_index  : enter_index2]
