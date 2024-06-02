#import random
from random import choices
import pyinputplus as pyip

def main():
	fname = "names.txt"
	# use with..as can auto close file object when exits the block
	with open(fname) as f:
		content = f.read()
		nlst = content.split()
		k = pyip.inputInt("How many name you want select? ", min=1)
		nlst_random = choices(nlst, k=k)
		n = pyip.inputMenu(nlst_random, prompt=f"請選擇姓名代碼 (1~{k}): \n", numbered=True)
		#print(f"n: {n}, type: {type(n)}")
		idx = nlst_random.index(n)
		print(f"You choice #{idx+1} {n}")

	print("End of practice")

if __name__ == '__main__':

	main()
