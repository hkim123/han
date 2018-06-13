#! /usr/bin/env/python3

import sys
import chilkat

#  This example assumes Chilkat SSH/SFTP to have been previously unlocked.
#  See Unlock SSH for sample code.

ssh = chilkat.CkSsh()

port = 22
success = ssh.Connect("leo-pst-1",port)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Authenticate using login/password:
success = ssh.AuthenticatePw("root","test123")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Start several commands on the server.
channel1 = ssh.QuickCmdSend("df")
if (channel1 < 0):
    print(ssh.lastErrorText())
    sys.exit()

channel2 = ssh.QuickCmdSend("date")
if (channel2 < 0):
    print(ssh.lastErrorText())
    sys.exit()

channel3 = ssh.QuickCmdSend("echo hello world")
if (channel3 < 0):
    print(ssh.lastErrorText())
    sys.exit()

#  Now collect the results of each command.
pollTimeoutMs = 50
numFinished = 0
while numFinished < 3 :
    #  Check to see if anything has finished.
    #  QuickCmdCheck returns -1 if there are no errors and nothing else finished
    #  QuickCmdCheck returns -2 if there was an error (such as a lost connection)
    #  QuickCmdCheck returns a channel number if a channel finished.
    channel = ssh.QuickCmdCheck(pollTimeoutMs)
    if (channel == -2):
        print(ssh.lastErrorText())
        sys.exit()

    if (channel >= 0):
        print("---- channel " + str(channel) + " finished ----")
        print(ssh.getReceivedText(channel,"ansi"))
        numFinished = numFinished + 1
