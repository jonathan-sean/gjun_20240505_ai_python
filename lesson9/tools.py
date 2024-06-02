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
