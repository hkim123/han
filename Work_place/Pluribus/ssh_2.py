#! /usr/bin/env/python3

import paramiko
import cmd

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('leo-pst-1', username='root', password='test123')


