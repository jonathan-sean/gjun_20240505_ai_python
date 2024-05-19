import pyinputplus as pyip

SCORE_MIN = 0
SCORE_MAX = 100
SCORE_WEIGHT = 1.05
SCORE_RANGE=f"{SCORE_MIN}~{SCORE_MAX}"

chinese = pyip.inputInt(f"請輸入國文成績({SCORE_RANGE}): ", min=SCORE_MIN, max=SCORE_MAX)
math = pyip.inputInt(f"請輸入數學成績({SCORE_RANGE}): ", min=SCORE_MIN, max=SCORE_MAX)

# 二科都 100 獎金 1000
# 一科 100 獎金 300
if chinese == SCORE_MAX and math == SCORE_MAX:
	bonus = 1000
elif chinese == SCORE_MAX or math == SCORE_MAX:
	bonus = 300
else:
	bonus = 0
print(f"獎金: {bonus}元")
