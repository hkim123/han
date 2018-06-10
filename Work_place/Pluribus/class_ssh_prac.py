#! /usr/local/bin/python3

from paramiko import client
import time




class ssh:
    client = None
 
    def __init__(self, address, username):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, username=username, look_for_keys=True)
 
    def sendCommand(self, command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata
 
                    print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")



connection = ssh("leo-pst-3","root")

file = open("/Users/hakim/python/pluribus/conf_leo_10.txt","r+")
lines = file.readlines() 
for line in lines:
	print(line)
	connection.sendCommand(line)
	time.sleep(5)
#file.write("this is test.\n")
file.close()



#print ("bootenv-show")
#connection.sendCommand(line_1)
#time.sleep(2)
#print ("pkg info pn-nvos")
#connection.sendCommand("pkg info pn-nvos")
#time.sleep(2)
#print("fabric node show")
#connection.sendCommand("cli fabric-node-show")

