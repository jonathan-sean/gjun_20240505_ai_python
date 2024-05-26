import random
import pyinputplus as pyip

# None means no return,
# can ignore this if no return value
def sayHello(n:str)->None:
	name:str = n
	print(f"Hello, {name}!")

# None means no return
def turn_home_light_on()->None:
	print("Turn on the light in my home")

def sum(a, b) -> int:
	return a+b

def getRandomNum()->float:
	return random.random()

def multiply(a:int, b:int)->int:
	return a*b

def print_factor(n:int):
	print(f"{n} 的因數有 ", end='')
	for i in range(1, n+1):
		if n % i == 0:
			if i >= n:
				print(i)
			else:
				print(i, end=', ')

sayHello("John")	# just assign argument
sayHello(n="Tom")	# assign argument to specific parameter
print(str.format("3 + 4 = {}", sum(3, 4)))
print(getRandomNum())
print(str.format("3 x 4 = {}", multiply(3, 4)))
print(str.format("3 x 4 = {}", multiply(b=3, a=4)))

try:
	n = pyip.inputInt(f"請輸入整數，求所有的公因數: ", min=1)
	print_factor(n)
except Exception as e:
	print(f"EXCEPTION - {type(e)}")
