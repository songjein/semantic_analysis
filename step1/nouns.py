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
	print (" ".join(komoran.nouns(line)))
