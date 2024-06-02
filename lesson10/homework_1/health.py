# BMI 計算 (with function)
# BMI = weight(kg) / height(m)^2

class BMI:
	__name: str
	__height: float
	__weight: float
	@property
	def name(self):
		return self.__name
	@property
	def height(self):
		return self.__height
	@property
	def weight(self):
		return self.__weight
	def setName(self, name:str):
		self.__name = name
	def setHeight(self, height:float):
		self.__height = height
	def setWeight(self, weight:float):
		self.__weight = weight
	def bmi(self)->float:
		return self.__weight / (self.__height / 100)**2
	def status(self, bmi: float)->str:
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
