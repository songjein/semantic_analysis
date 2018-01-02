# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from konlpy.tag import Komoran

# get from result of Translator + ConceptNet
ConceptNet = {'HasA': [{'weight': 6.32455532033676, 'term': '좌석'}, {'weight': 2.82842712474619, 'term': '앉은 자리'}, {'weight': 2.82842712474619, 'term': '창문들'}, {'weight': 2.0, 'term': '발동기'}, {'weight': 2.0, 'term': '가시성을 높이기 위한 헤드 라이트'}, {'weight': 1.0, 'term': '타이어 4개'}, {'weight': 1.0, 'term': '적어도 하나 이상의 엔진'}, {'weight': 1.0, 'term': '엔진의 동력을 끄는 기관'}, {'weight': 1.0, 'term': '거름 종이'}, {'weight': 1.0, 'term': '타이어 4개'}], 'IsA': [{'weight': 4.47213595499958, 'term': '볼보보'}, {'weight': 3.4641016151377544, 'term': '혼다'}, {'weight': 3.4641016151377544, 'term': '망망한 사람'}, {'weight': 2.82842712474619, 'term': 'BMW자동차'}, {'weight': 2.82842712474619, 'term': '자동차'}, {'weight': 2.82842712474619, 'term': 'A차'}, {'weight': 2.82842712474619, 'term': '폭스바겐'}, {'weight': 2.0, 'term': '구급차'}, {'weight': 2.0, 'term': '수하물 차'}, {'weight': 2.0, 'term': '비치 왜건'}], 'PartOf': [{'weight': 4.47213595499958, 'term': 'A타이어'}, {'weight': 3.4641016151377544, 'term': '범퍼'}, {'weight': 3.4641016151377544, 'term': '엔진'}, {'weight': 2.82842712474619, 'term': '뿔'}, {'weight': 2.82842712474619, 'term': '바퀴'}, {'weight': 2.0, 'term': '가속기'}, {'weight': 2.0, 'term': '에어 백'}, {'weight': 2.0, 'term': '오토 액세서리'}, {'weight': 2.0, 'term': '자동차 엔진'}, {'weight': 2.0, 'term': '자동차 경적'}]}

Relations = ["HasA", "IsA", "PartOf"]

NN_SL = ["NN", "SL"]

komoran = Komoran()

def termsOf(relation):
	return [wt["term"] for wt in ConceptNet[relation]]

def isNN_SL(tag):
	return ("NNG" == tag) or ("SL" == tag) or ("NNP" == tag)

def showList(l):
	print (",".join([i for i in l]))

# preprocess ConceptNet's terms
# filter ConceptNet result to get only NN or SL (foreign language)
# because translation have some noise 
# POS 태거의 성능 의존 --> 범퍼는 범 푸 어 로 해석되어서 필터링 아웃 됨
# word2vec으로 확장할 때, 추가되길 기대할 수 밖에

def preprocess(verbose=True):
	print ("ConceptNet preprocessing...")
	ret = {} 
	for r in Relations:
		tmp = []
		terms = termsOf(r)
		if verbose: print ("\n\nOriginal Terms of " + r)
		if verbose: print (" ,".join(terms))
		for t in terms: 
			tagList = komoran.pos(t)
			if verbose: print (" ".join(["%s/%s"%(tag[0],tag[1])for tag in tagList]))
			nouns_sl_list = [tag for tag in tagList if isNN_SL(tag[1])]
			if verbose: print (t + " --> " + ", ".join(["%s/%s"%(item[0],item[1]) for item in nouns_sl_list]))
			tmp += nouns_sl_list
		if verbose: print ("\nPreprocessed result")
		noDup = list(set([i[0] for i in tmp]))
		if verbose: print (" ".join(noDup))
		ret[r] = noDup
	if verbose: print ("\n\nFinal result")
	if verbose: print (ret)
	return ret


if __name__ == "__main__":
	preprocess()
