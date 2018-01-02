# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import openpyxl

wb = openpyxl.load_workbook('wise.xlsx')

ws = wb.active

for r in ws.rows:
	print (r[0].value)
