# -*- coding:utf8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from itertools import chain

from konlpy.tag import Komoran

import conceptNet

"""
	ConceptNet의 후보를 가지면서,
	VA를 포함하는 문장을 걸러낸다
"""

f = open("../step1/wise_pos.txt") # pos
f_n_p = open("../step1/wise.txt") # no pos

# seed relations
seedRel = conceptNet.preprocess()

# make seed topic
seedTopic = []
for r in conceptNet.Relations:
	seedTopic += seedRel[r]

# seedTopic
seedTopic = list(set(seedTopic))

"""
 seedTopic extension with topic.txt 
 원래 목적은 컨셉넷 기반으로 확장
 현재는 seedTopic 자체에 확장
"""
'''
f_t = open("topic.txt")
topicsFromCoMatrix = f_t.read().split("\n")
topicsFromCoMatrix = [t.split(",") for t in topicsFromCoMatrix]
topicsFromCoMatrix = list(set(list(chain(*topicsFromCoMatrix))))
print (",".join(topicsFromCoMatrix))
print ("==============================")

seedTopic += topicsFromCoMatrix

# 노이즈 제거해야 됌
seedTopic = [t for t in seedTopic if len(t) > 2]

conceptNet.showList(seedTopic)
'''
# 마지막단계에서 사람의 수정(modified_topic.txt - 위에서 확장된 결과에서 직접 노이즈 제거 및 추가)
modified = ""
USE_MODIFIED_TOPIC = True
if USE_MODIFIED_TOPIC:
	f_m_t = open("modified_topic.txt")
	modified = f_m_t.readline()
	seedTopic = modified.split(",")
	print("modified topic set")
	conceptNet.showList(seedTopic)


# 주어진 문장이, subject를 포함하고, seedTopic 및 VA(형용사)를 포함하는지 체크한다
def filter_s_t_va(line, subject, verbose=False):
	if subject not in line: return False

	if verbose: print ("\n\n\n입력 문장 :")
	if verbose: print (line)
	if verbose: print ("========================================================================================================")

	subjectOk = False
	seedOk = False
	vaOk = False

	if subject in line:
		if verbose: print ("[주제어] %s를 %d개 포함합니다" %(subject, line.count(subject)))
		subjectOk = True
	for s in seedTopic:
		if len(s.strip()) > 0 and (s in line):
			if verbose: print (s + " 를 포함 합니다")
			seedOk = True
	if "VA" in line:
		if verbose: print ("[VA] 를 %d 개 포함 합니다" %(line.count("VA")))
		vaOk = True
	if verbose: print (subjectOk, seedOk, vaOk)
	return (subjectOk and seedOk and vaOk)

# 분석 대상 뭄장을 찾는다

# ex) 아반떼, 쏘나타, 그렌져 (필터링으로 모을 대상)
userInputSubject = raw_input("User's subject (예:아반떼--> 결과:아반떼_pos.txt, 아반떼_no_pos.txt):") 
'''
	이름_pos.txt 는 포스 태깅 된 것으로 필터링된 결과
	이름_no_pos.txt는 오리지널 버전으로 필터링된 결과
'''
wf = open("./%s_pos.txt"%(userInputSubject), "w")
wf_n_p = open("./%s_no_pos.txt"%(userInputSubject), "w") # no pos

while True:
	line = f.readline()
	line_n_p = f_n_p.readline()
	if not line: break
	# if filter_s_t_va(line, userInputSubject, True):
	if filter_s_t_va(line, userInputSubject):
		wf.write(line)
		wf_n_p.write(line_n_p)

