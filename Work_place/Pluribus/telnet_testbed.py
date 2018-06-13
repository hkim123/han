#!/usr/bin/python2.6

import telnetlib


R1 = "10.126.203.36"
R2 = "10.126.203.24"
R3 = "10.126.203.21"
R4 = "10.126.203.26"
R5 = "10.126.203.31"

user = "test"
password = "test"

######### R1 ##########

tn = telnetlib.Telnet(R1)

tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show version\n")
tn.write("show chassis\n")
#tn.write("washoutthewash\n")
tn.write("exit\n")

output = tn.read_all()
print output


############## R2 ##########


tn = telnetlib.Telnet(R2)

tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show version\n")
tn.write("show chassis\n")
tn.write("exit\n")

output = tn.read_all()
print output


############## R3 ##########


tn = telnetlib.Telnet(R3)

tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show version\n")
tn.write("show chassis\n")
tn.write("exit\n")

output = tn.read_all()
print output


############## R4 ##########


tn = telnetlib.Telnet(R4)

tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show version\n")
tn.write("show chassis\n")
tn.write("exit\n")

output = tn.read_all()
print output


############## R5 ##########


tn = telnetlib.Telnet(R5)

tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show version\n")
tn.write("show chassis\n")
tn.write("exit\n")

output = tn.read_all()
print output

