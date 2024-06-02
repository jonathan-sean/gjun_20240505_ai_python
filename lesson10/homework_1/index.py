import pyinputplus as pyip
from health import BMI

def main():
	INPUT_TRY = 3
	print("BMI 計算")
	# Exception handling refer to https://docs.python.org/3/tutorial/errors.html
	try:
		# Create class instance of BMI
		obj = BMI()
		# Input user information, include name, height and weight
		obj.setName(pyip.inputStr("請輸入姓名: ", limit=INPUT_TRY))
		obj.setHeight(pyip.inputFloat("請輸入身高(cm): ", min=0, limit=INPUT_TRY))
		obj.setWeight(pyip.inputFloat("請輸入體重(kg): ", min=0, limit=INPUT_TRY))

		# Calculate BMI and get result
		bmi = obj.bmi()
		status = obj.status(bmi)

		# Output user information, BMI and result
		#print(f"\n{obj.name} - \n身高: {obj.height}cm\n體重: {obj.weight}Kg")
		print(f"{obj.name} BMI 值為 {round(bmi, 2)}")
		print(f"您的體重: {status}")
	except Exception as e:
		print(f"ERROR - {type(e)}")


if __name__ == '__main__':
	main()
