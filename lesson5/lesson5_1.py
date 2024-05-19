# 學生的總分最高為 300分
# 若超過 300分則以 300分記
# 有些學生可以加 5%

try:
	scores = int(input("請輸入學生分數(最高300分):"))
	if scores > 300 or scores < 0:
		print("Input value over the range (0~300), please input again.")
	else:
		is_add = input("學生是否符合加分條件?(y/n)")
		if is_add == 'y':
			scores *= 1.05
		if scores > 300:
			scores = 300

		print(f"學生分數是: {round(scores, 0)}")
except ValueError:
	print("Invalid value, check your input.")
except Exception as e:
	print(f"Exception: {type(e)}, check your input.")
print("End this program.")
