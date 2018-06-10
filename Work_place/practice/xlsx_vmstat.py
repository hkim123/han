#!/usr/bin/python2.7
#coding=utf-8

from subprocess import * 
from xlsxwriter import *

cmd = "vmstat 1 5 | awk '{now=strftime(\"%Y-%m-%d %T \"); print now $0}'"
p = Popen(cmd, shell=True, stdout=PIPE)
(ret, err) = p.communicate()

workbook = Workbook('vmstat.xlsx')
worksheet = workbook.add_worksheet()
rows = ret.split("\n")

for row_idx, row in enumerate(rows) :
	colums = row.split()
	for col_idx, col in enumerate(colums) :
	    worksheet.write(row_idx, col_idx, col)

workbook.close()
