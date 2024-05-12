# BMI 計算, refer to https://toolboxtw.com/zh-TW/calculator/bmi
# BMI = weight(kg) / height(m)^2

print("BMI 計算，請輸入")
# Input name
name = input("姓名: ")
# Input height
height = float(input("身高(公分): "))
# Input weight
weight = float(input("體重(公斤): "))

# Output user information
bmi = weight / (height / 100)**2
# Get the result
if bmi < 18.5:
	result = "過輕"
elif bmi >= 18.5 and bmi < 24:
	result = "正常"
elif bmi >= 24 and bmi < 27:
	result = "過重"
else:
	result = "肥胖"

# Output BMI and result
print(f"\n{name} - 身高: {height}cm，體重: {weight}Kg， BMI: {round(bmi, 2)}({result})")
