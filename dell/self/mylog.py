#!/usr/bin/python

def printlog(logfile, word):
	f = open(logfile)
	logdata = f.read()
	f.close()

	index = logdata.find(word)
	if index >= 0 :
		print "-" * 70
    		print "Log file: " , logfile
    		print "Find this word: ", word
		print index
    		print "-" * 70
	else:
		print "No word"
