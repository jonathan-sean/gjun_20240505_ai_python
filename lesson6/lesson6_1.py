# 學生的總分最高為 300分
# 若超過 300分則以 300分記
# 有些學生可以加 5%
# 成績等級
#  90~100 優
#  80~89  甲
#  70~79  乙
#  60~69  丙
#  0~59  丁

import pyinputplus as pyip

SCORE_MIN = 0
SCORE_MAX = 100
SCORE_WEIGHT = 1.05
SCORE_RANGE=f"{SCORE_MIN}~{SCORE_MAX}"

try:
	score = pyip.inputInt(f"請輸入學生分數({SCORE_RANGE}): ", min=SCORE_MIN, max=SCORE_MAX, timeout=10)
	is_add = pyip.inputStr("學生是否符合加分條件?(y/n) ", timeout=5, allowRegexes="y|n")
	if is_add == 'y':
		score *= SCORE_WEIGHT
	if score > SCORE_MAX:
		score = SCORE_MAX

	if score >= 90:
		grade = "優"
	elif score >= 80:
		grade = "甲"
	elif score >= 70:
		grade = "乙"
	elif score >= 60:
		grade = "丙"
	else:
		grade = "丁"

	print(f"學生分數是: {round(score, 0)} ({grade}等)")
except pyip.TimeoutException:
	print("ERROR - Input timeout.");
except A:
	print(f"ERROR: Input over range ({SCORE_RANGE}) ...")
except Exception as e:
	print(f"Exception: {type(e)}, check your input.")
	#print(f"Exception: {e}, check your input.")

print("End this program.")
