# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from konlpy.tag import Komoran

f = open("wise.txt")

komoran = Komoran()

while True:
	line = f.readline()
	if not line: break
	tmp = []
	for t in komoran.pos(line):
		s = t[0] + "/" + t[1]
		tmp.append(s)
	print (" ".join(tmp))
		
