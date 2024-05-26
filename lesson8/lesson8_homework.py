# BMI 計算 (with function)
# BMI = weight(kg) / height(m)^2

import pyinputplus as pyip

def cal_bmi(height:float, weight:float)->float:
	return weight / (height / 100)**2

def get_status(bmi: float)->str:
	if bmi < 18.5:
		return "過輕"
	elif bmi >= 18.5 and bmi < 24:
		return "正常"
	elif bmi >= 24 and bmi < 27:
		return "過重"
	elif bmi >= 27 and bmi < 30:
		return "輕度肥胖"
	elif bmi >= 30 and bmi < 35:
		return "中度肥胖"
	return "重度肥胖"


INPUT_TRY = 3

print("BMI 計算，請輸入")
# Exception handling refer to https://docs.python.org/3/tutorial/errors.html
try:
	# Input user information, include name, height and weight
	name = pyip.inputStr("姓名: ", limit=INPUT_TRY)
	height = pyip.inputFloat("身高(公分): ", min=0, limit=INPUT_TRY)
	weight = pyip.inputFloat("體重(公斤): ", min=0, limit=INPUT_TRY)

	# Calculate BMI and get result
	bmi = cal_bmi(height, weight)
	status = get_status(bmi)

	# Output user information, BMI and result
	print(f"\n{name} - \n身高: {height}cm\n體重: {weight}Kg")
	print(f"BMI: {round(bmi, 2)}  體重{status}")
except Exception as e:
	print(f"EXCEPTION - {type(e)}")
