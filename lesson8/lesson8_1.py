import random
import pyinputplus as pyip	# The usage refer to https://github.com/asweigart/pyinputplus/blob/master/src/pyinputplus/__init__.py

def play_game(start:int, stop:int):
	count:int = 0
	hint:bool = False	# let user guess easier

	target = random.randint(start, stop)
	print("----------- Guessing Number Game -----------")
	while(True):
		count += 1
		keyin = pyip.inputInt(f"Guess#{count}: Input your number ({start}~{stop}): ", min=start, max=stop)
		if(keyin > target):
			print("Too large ...")
			if hint: stop = keyin - 1
			continue
		if(keyin < target):
			print("Too small ...")
			if hint: start = keyin + 1
			continue
		print("You win!")
		break
	print(f"You guess {count} times")

while(True):
	play_game(1, 100)
	again = pyip.inputYesNo("Play again? ", default='n', yesVal='y', noVal='n')
	if again == "n":
		break

print("Thanks for your playing.")
