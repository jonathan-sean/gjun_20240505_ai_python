class Person:
	'''class Person - A simple class example'''
	# Custom initial
	def __init__(self, name="Ghost"):
		print("This is initial method")
		self.name = name
	def __repr__(self):
		return f"My name is {self.name}"

class Student(Person):
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

class College(Student):
	def __repr__(self):
		msg = super().__repr__();
		msg += " (College))"
		return msg
	@property
	def chemical(self):
		return self.__chemical
	def setChemical(self, chem:int):
		self.__chemical = chem
	def sum(self):
		return super().sum()+self.__chemical
	def average(self)->float:
		return round(self.sum()/4, 2)

print(Person.__doc__)
print(Person.__name__)

p1:Person = Person("Hank")
#print(type(p1))
print(p1.name)
print(p1)

p2 = Person("Mary")
#print(type(p2))
print(p2.name)
print(p2)

p3 = Person()
print(p3.name)
print(p3)

print(Student.__doc__)
s1 = Student("Hank", ch=60, en=80, ma=50)
print(s1.name)
# Below will fail, chinese is private
#s1.chinese = 100
print(s1)
#print(type(s1))
print(f"Chinese: {s1.chinese}")
print(f"English: {s1.english}")
print(f"Math: {s1.math}")
print(f"Total: {s1.sum()}")
print(f"Average: {s1.average()}")

s2 = Student("Tom", 80, 90, 99)
print(s2.name)
print(s2)
#print(type(s2))
print(f"Chinese: {s2.chinese}")
print(f"English: {s2.english}")
print(f"Math: {s2.math}")
print(f"Total: {s2.sum()}")
print(f"Average: {s2.average()}")

s3 = College("John", 90, 90, 99);
print(s3)
s3.setChemical(88)
print(f"Chinese: {s3.chinese}")
print(f"English: {s3.english}")
print(f"Math: {s3.math}")
print(f"Chemical: {s3.chemical}")
print(f"Total: {s3.sum()}")
print(f"Average: {s3.average()}")
