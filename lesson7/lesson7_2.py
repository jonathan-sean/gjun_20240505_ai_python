import random
import pyinputplus as pyip

min:int = 1
max:int = 10

target = random.randint(min, max)
print("----------- Guessing Number Game -----------")
while(True):
	keyin = pyip.inputInt(f"Input your number ({min}~{max}): ", min=min, max=max)
	if(keyin > target):
		print("Too large ...")
		continue
	if(keyin < target):
		print("Too small ...")
		continue
	print("You win!")
	break

print("Game Over")
