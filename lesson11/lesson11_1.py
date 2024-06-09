import json
from pprint import pprint

def practice1():
	fpath:str = "aqx_p_488.json"
	fname:str = fpath.removesuffix(".csv")
	print(f"[practice1] JSON: {fname}")
	with open(fpath, encoding='UTF-8') as f:
		json_content:str = f.read()
		# store any dictionary data from json_content
		data:dict[any] = json.loads(json_content)
		# get data from field records
		records:list[dict] = data['records']
		for r in records:
			pprint(r)

def practice2():
	fpath:str = "aqx_p_488.json"
	fname:str = fpath.removesuffix(".csv")
	print(f"[practice2] JSON: {fname}")

def main():
	practice1()

if "__main__" == __name__:
	main()
