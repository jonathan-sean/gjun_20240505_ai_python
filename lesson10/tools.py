# constant
PI = 3.1415926

# method
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

# class
class __Person:
	'''class Person - A simple class example'''
	# Custom initial
	def __init__(self, name="Ghost"):
		print("This is initial method")
		self.name = name
	def __repr__(self):
		return f"My name is {self.name}"

class Student(__Person):
	'''class Student - A simple class inherence example'''
	# x: public attribute
	# _x: protected attribute
	# __x: private attribute
	def __init__(self, name:str, ch:int, en:int, ma:int):
	# x: public attribute
		# Call __init__ of parent
		super().__init__(name)
		self.__chinese = ch
		self.__english = en
		self.__math = ma
	def __repr__(self):
		msg = super().__repr__();
		msg += ", I'm a student."
		return msg
		#return f"My name is {self.name}\nChinese: {self.chinese}, English: {self.english}, Math: {self.math}"
	@property
	def chinese(self) -> int:
		return self.__chinese
	@property
	def english(self) -> int:
		return self.__english
	@property
	def math(self) -> int:
		return self.__math
	def sum(self) -> int:
		return self.chinese+self.english+self.math
	def average(self)->float:
		return round(self.sum()/3, 2)

def get_student(name, chinese, english, math)->Student:
	return Student(name, chinese, english, math)
