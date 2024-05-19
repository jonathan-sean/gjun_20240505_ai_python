# 學生的總分最高為 300分
# 有些學生可以加 5%

scores = int(input("請輸入學生分數(最高300分):"))
is_add = input("學生是否符合加分條件?(y/n)")
if is_add == 'y':
	scores *= 1.05

print(f"學生分數是: {round(scores, 0)}")
