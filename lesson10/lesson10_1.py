#import random
from random import choices
import pyinputplus as pyip

def main():
	fname = "names.txt"
	f = open(fname)
	print(type(f))
	print(f"{fname} is closed? {f.closed}")
	f.close()
	print(f"{fname} is closed? {f.closed}")

	# use with..as can auto close file object when exits the block
	with open(fname) as f:
		content = f.read()
		#print(f"Full content: \n{content}")
		f.seek(0)
		print(f"First line: {f.readline().strip()}")
		f.seek(0)
		for l in f:
			print(l.strip(), end='\t')
		print()
		nlst = content.split()
		print(f"Amount: {len(nlst)}")
		print(f"Top 5 names: {nlst[0:5]}")
		print(f"Last 5 names: {nlst[-5:]}")
		print(f"Random: {choices(nlst)}")
		k = pyip.inputInt("How many name you want select? ", min=1)
		#print(f"Random {k}: {choices(nlst, k=5)}")
		nlst_random = choices(nlst, k=k)
		n = pyip.inputMenu(nlst_random, prompt=f"請選擇姓名代碼 (1~{k}): \n", numbered=True)
		#print(f"n: {n}, type: {type(n)}")
		idx = nlst_random.index(n)
		print(f"You choice #{idx+1} {n}")
		print(f"[Inner with..as block] {fname} is closed? {f.closed}")
	print(f"[Outer with..as block] {fname} is closed? {f.closed}")

	print("End of practice")

if __name__ == '__main__':
	main()
