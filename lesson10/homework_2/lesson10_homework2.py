import csv
import pyinputplus as pyip
from pprint import pprint
from random import choices

def main():
	fname = "個股日成交資訊.csv"
	with open(fname, encoding="UTF-8", newline='') as f:
		reader = csv.DictReader(f)
		lst = list(reader)
		print(str.format("{}共有 {} 筆資料", fname.removesuffix(".csv"), len(lst)))
		# Too much data, just show some to demonstration
		n = pyip.inputInt("請輸入要隨機顯示的資料數(1~20): ", min=1, max=20)
		lst_2 = choices(lst, k=n)
		for d in lst_2:
			# Get index of complete data
			idx = lst.index(d)
			print(f"#{idx}")
			pprint(d, indent=2, sort_dicts=False)
'''
		f.seek(0)
		header = f.readline().strip()
		for h in header.split(','):
			print("{:9}".format(h), end='')
		print("\n--------------------------------------------------")
		#print(str.format("{}", header.replace(',', '\t')))
		for e in lst[1:6]:
			for v in e.values():
				print("{:<11}".format(v), end='')
			print()
'''


if '__main__' == __name__:
	main()
