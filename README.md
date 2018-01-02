# semantic_analysis

wise.xlsx (451MB exel file, crawled data)

## step1
- read "wise.xlsx" exel file using exel.py
-- python exel.py >> "wise.txt"
- extract nouns using nouns.py
-- python nouns.py >> "wise_nouns.txt"
- add tagging using pos.py
-- python pos.py >> "wise_pos.txt"


## step2
- filter in candidate sentences using filter.py
-- python filter.py
-- > 아반떼
-- output: 아반떼_pos.txt, 아반떼_no_pos.txt
- do semantic analysis using semantic.py
-- python semantic.py
-- > 아반떼
-- output: html file
