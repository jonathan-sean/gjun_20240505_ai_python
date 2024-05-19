# BMI 計算, refer to https://toolboxtw.com/zh-TW/calculator/bmi
# BMI = weight(kg) / height(m)^2

import pyinputplus as pyip

INPUT_TRY = 3

print("BMI 計算，請輸入")
# Exception handling refer to https://docs.python.org/3/tutorial/errors.html
try:
	# Input user information, include name, height and weight
	name = pyip.inputStr("姓名: ", limit=INPUT_TRY)
	height = pyip.inputFloat("身高(公分): ", min=0, limit=INPUT_TRY)
	weight = pyip.inputFloat("體重(公斤): ", min=0, limit=INPUT_TRY)

	# Calculate BMI and get result
	bmi = weight / (height / 100)**2
	if bmi < 18.5:
		result = "過輕"
	elif bmi >= 18.5 and bmi < 24:
		result = "正常"
	elif bmi >= 24 and bmi < 27:
		result = "過重"
	else:
		result = "肥胖"

	# Output user information, BMI and result
	print(f"\n{name} - 身高: {height}cm，體重: {weight}Kg， BMI: {round(bmi, 2)}")
	print(f"你的體重{result}")
except Exception as e:
	print(f"EXCEPTION - {type(e)}")
