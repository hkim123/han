#!/usr/bin/python2.7

from xlsxwriter import *

workbook = Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
data = '1 2 3 4 5'

colums = data.split()
for col_idx, col in enumerate(colums) :
    worksheet.write(0, col_idx, col)

workbook.close()


