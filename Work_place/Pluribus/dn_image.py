#!/usr/bin/python

import telnetlib
import datetime
import time


now = datetime.datetime.now()
HOST_1 = "10.126.210.176"  ### XFT PE-A
user = "test"
password = "test"
dn_rp = "scp ehankim@10.10.10.22://archive/build-images/lsv/IPOS-pc-linux-ref-rp-16.1.0.100.386.tar.gz ."
dn_lc = "scp ehankim@10.10.10.22://archive/build-images/lsv/IPOS-pc-linux-ref-lc-16.1.0.100.386.tar.gz ."
inst = "/usr/lib/siara/bin/dfm_client all /md/IPOS-pc-linux-ref-rp-16.1.0.100.386.tar.gz /md/IPOS-pc-linux-ref-lc-16.1.0.100.386.tar.gz update "
filename_prefix = "image_upgrade"
sh = "start shell"

tn = telnetlib.Telnet(HOST_1)


tn.read_until("login: ")
tn.write(user + "\n")

tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("enable\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("\n")

#tn.write("show version\n")
tn.write("show configuration\n")

tn.write("st sh"+ "\n\r")
time.sleep(5)
tn.write("\n\r")
tn.write("\n\r")
tn.write("cd /md"+ "\n\r")
time.sleep(5)
tn.write("\n\r")
tn.write("ls -lrt"+ "\n\r")
tn.write("\n\r")

### download RP image
tn.write(dn_rp + "\n\r")
time.sleep(5)
##tn.read_until("ehankim@10.10.10.22's password: ")
tn.write("Arbor2825" + "\n\r")

time.sleep(60)
tn.read_until("root@Ref_6d01-ipos3-pe-b:/md# ")


#### Download lc image
tn.write(dn_lc + "\n\r")
time.sleep(5)
##tn.read_until("ehankim@10.10.10.22's password: ")
tn.write("Arbor2825" + "\n\r")

time.sleep(60)
tn.read_until("root@Ref_6d01-ipos3-pe-b:/md# ")

#### install new image
tn.write(inst + "\n\r")
time.sleep(30)
tn.read_until("root@Ref_6d01-ipos3-pe-b:/md# ")

tn.write("exit"+"\n")

tn.write("\n")

tn.write("exit"+"\n")
tn.write("exit"+"\n")
output = tn.read_all()
print output

filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
fp = open(filename, "w")
fp.write(output)
fp.close()

'''
tn.write("start shell\n")
tn.read_until("root@Ref_6d01-ipos1-pe-a:/flash# ")
tn.write("\n")
tn.write("\n")
tn.write("exit"+"\n")
output = tn.read_all()
filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
fp = open(filename, "w")
fp.write(output)
fp.close()



tn.read_until("[local]Ref_6d01-ipos1-pe-a#")

tn.write("start shell\n")
tn.read_until("root@Ref_6d01-ipos1-pe-a:/flash# ")
tn.write("\n")
tn.write("\n")
tn.write("dir\n")
tn.write("cd /md\n")
tn.write("\n")
tn.read_until("root@Ref_6d01-ipos1-pe-a:/md# ")
tn.write("dir\n")
raw_input("press anykey here....")

#tn.write("dir \n")


#tn.read_until(



tn.write("exit\n")
tn.write("exit\n")

print tn.read_all()

'''
