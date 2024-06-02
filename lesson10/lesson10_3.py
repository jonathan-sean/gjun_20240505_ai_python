import csv
from pprint import pprint

def main():
	fname = "tw-hospitals.csv"
	with open(fname, encoding="UTF-8", newline='') as f:
#		content = f.read()
#		print(content)
		reader = csv.DictReader(f)
		lst = list(reader)
		pprint(lst)


if '__main__' == __name__:
	main()
