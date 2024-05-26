import random
import pyinputplus as pyip	# The usage refer to https://github.com/asweigart/pyinputplus/blob/master/src/pyinputplus/__init__.py

min:int = 1
max:int = 100
count:int = 0
hint:bool = False	# let user guess easier

while(True):
	target = random.randint(min, max)
	print("----------- Guessing Number Game -----------")
	while(True):
		count += 1
		keyin = pyip.inputInt(f"Guess#{count}: Input your number ({min}~{max}): ", min=min, max=max)
		if(keyin > target):
			print("Too large ...")
			if hint: max = keyin - 1
			continue
		if(keyin < target):
			print("Too small ...")
			if hint: min = keyin + 1
			continue
		print("You win!")
		break
	print(f"You guess {count} times")
	again = pyip.inputYesNo("Play again? ", default='n', yesVal='y', noVal='n')
	if again == "n":
		break

print("Thanks for your playing.")
