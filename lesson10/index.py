import tools
from tools import Student

class Student1(tools.__Person):
	pass

def main():
	print(tools.PI)
	s1:Student = tools.get_student("Hans", 80, 90, 70)
	print(s1)
	print(f"Chinese: {s1.chinese}")
	print(f"English: {s1.english}")
	print(f"Math: {s1.math}")
	print(f"Total: {s1.sum()}")
	print(f"Average: {s1.average()}")

	s2 = Student1("Tom")
	print(s2)

if __name__ == '__main__':
	main()
