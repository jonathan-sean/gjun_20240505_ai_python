# nested structure
from pprint import pprint

print("list in list")
students = [
	["John", 90, 50, 80],
	["Johnson", 80, 70, 80],
	["Hank", 99, 87, 85],
]

print(str.format("student type: {}", type(students)))
print(f"students: {students}")
for s in students:
	print(s)
print("Print with pprint")
pprint(students)

print("\ndict in list")
students = [
	{'name':"John", 'English':90, 'Chinese':50, 'math':80},
	{'name':"Johnson", 'English':80, 'Chinese':70, 'math':80},
	{'name':"Hank", 'English':99, 'Chinese':87, 'math':85},
]
print(f"students: {students}")
for s in students:
	print(s)
print("Print with pprint")
pprint(students)
