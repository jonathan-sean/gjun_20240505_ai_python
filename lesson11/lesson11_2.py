# data class

def practice1():
	class Student(object):
		def __init__(self, name:str, scores: int):
			self.name = name
			self.scores = scores
		def __repr__(self):
			msg:str = ""
			msg += f"My name is {self.name}\n"
			msg += f"My scores is {self.scores}\n"
			return msg

	s1:Student = Student("Tom", 390)
	print(s1)

def practice2():
	from dataclasses import dataclass

	@dataclass
	class Student(object):
		name:str
		scores:int = 0

	s1:Student = Student("Tom", 390)
	print(s1)
	s2:Student = Student("Kent")
	print(s2)

def practice3():
	# pydantic refer to https://docs.pydantic.dev
	# BaseModel inherited from dataclass, but the first parameter is '*'
	# BaseMode will auto convert data type,
	# for example the file is int, when I input a str, BaseMode will convert it to int automatically
	from pydantic import BaseModel

	class Student(BaseModel):
		name:str
		scores:int = 0

	s1:Student = Student(name="Tom", scores=390)
	print(s1)
	s2:Student = Student(name="Kent")
	print(s2)
	s3:Student = Student(name="Hans", scores="320")
	print(s3)


if '__main__' == __name__:
#	practice1()
#	practice2()
	practice3()
