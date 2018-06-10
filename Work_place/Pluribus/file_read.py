#! /usr/local/bin/python3

file = open("/Users/hakim/python/pluribus/conf_leo_10.txt","r")
lines = file.readlines() 
for line in lines:
	print(line)
#	connection.sendCommand(line)
#	time.sleep(5)
#file.write("this is test.\n")
file.close()