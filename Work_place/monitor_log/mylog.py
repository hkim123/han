#!/usr/bin/python
#find fail from the log and display before and after lines, It works with exec_mylog.py, run ./exec_mylog
def printlog(logfile, search_word, pre_rowcount, next_rowcount):
    f = open(logfile)
    logdata = f.read()
    f.close

    index = logdata.find(search_word)
    if index >= 0 :

        print "-" * 70
        print "Log file: " , logfile
        print "Find this word: ", search_word
        #print index  #number of character not line 590
        print "-" * 70

        print get_log_data(logdata, index, pre_rowcount, next_rowcount)
        print "-" * 70

def get_log_data(logdata,start_index, pre_rowcount, next_rowcount) :
    enter_index = max(0,logdata.rfind("\n", 0, start_index ))
    for i in range(0, pre_rowcount):
        enter_index= max(0,logdata.rfind("\n", 0, enter_index ))
#        print enter_index

    enter_index2 = logdata.find("\n", start_index, len(logdata))
    for i in range(0, next_rowcount):
        next_end_index2=logdata.find("\n", enter_index2 + 1, len(logdata))
        if next_end_index2 == -1 :
            next_end_index2 = enter_index2
            break
        else :
            enter_index2 = next_end_index2

    return logdata[enter_index  : enter_index2]
