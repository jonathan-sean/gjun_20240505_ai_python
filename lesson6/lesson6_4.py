import pyinputplus as pyip

deposit = 0
n = 0
while deposit < 30000:
	try:
		n += 1
		income = pyip.inputInt(f"請輸入第{n}次存入金額: ", min=0, limit=2)
		deposit += income
	except Exception as e:
		print(f"EXCEPTION - {type(e)}")
		break

print(f"你已在 {n} 個月中存了 {deposit}元")

# Endless while loop with break
while True:
	v = pyip.inputStr("Please input your data ('q' to quit): ")
	if v == 'q':
		break
	print(f"Your input is {v}")

while True:
	v = input("Please input integer ('q' to quit): ")
	if v == 'q':
		break
	try:
		vi = int(v)
	except Exception as e:
		print("ERROR - Something wrong, try again.")
		continue
	print(f"Your input is {vi}")

print("The End")
