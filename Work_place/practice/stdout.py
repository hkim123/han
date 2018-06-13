#!/usr/bin/python
import sys

args = ['ls','-alh']
sys.stdout = open("result.txt", "w")
sys.stdout.flush()
process = subprocess.Popen(args1, shell=False,stdout=sys.stdout)
process.wait()
