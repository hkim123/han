#!/usr/bin/python
#this script for find fail from the log and display before and after lines, It works with exec_failing_argu4.py, run ./exec_failing_argu4.py

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

        (data, count) = get_log_data(logdata, search_word, index, pre_rowcount, next_rowcount)
        print data
        print "Total number of extract log : " , count

def get_log_data(logdata, search_word, start_index, pre_rowcount, next_rowcount) :
    count = 0
    ret = ""
    while start_index >= 0 :
        enter_index = max(0,logdata.rfind("\n", 0, start_index ))

        for i in range(0, pre_rowcount):
            enter_index= max(0,logdata.rfind("\n", 0, enter_index ))

        enter_index2 = logdata.find("\n", start_index, len(logdata))
        for i in range(0, next_rowcount):
            next_end_index2=logdata.find("\n", enter_index2 + 1, len(logdata))
            if next_end_index2 == -1 :
                next_end_index2 = enter_index2
                break
            else :
                enter_index2 = next_end_index2
        ret = ret + logdata[enter_index : enter_index2]
        ret = ret + "\n" + ("-"  * 70)
        start_index = logdata.find(search_word, enter_index2 + 1)
        count = count + 1
    return (ret, count)
