#!/usr/bin/python2.4

import telnetlib


HOST = "pipd-ssr-98.eld"
user = "test"
password = "test"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("show version\n")
tn.write("exit\n")

print tn.read_all()


