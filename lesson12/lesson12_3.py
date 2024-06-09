# Verify and convert CSV to Python list data by PyDantic
from csv import DictReader
from pydantic import (
	BaseModel,
	RootModel,
	Field,
	ValidationError,
	field_validator
)
from pprint import pprint

def get_csv_list(fp:str) -> list[dict]|None:
	with open(fp, encoding="UTF-8", newline='') as f:
		reader:DictReader = DictReader(f)
		# Must convert to list here
		return list(reader)

def practice1():
	class Stock(BaseModel):
		證券名稱:str;
		成交股數:int;
		成交金額:int;
		最低價:float;
		最高價:float;
		成交筆數:int;
		@field_validator("最低價", "最高價", "成交股數", "成交金額", "成交筆數", mode="before")
		@classmethod
		def remove_comma(cls, value:str) -> str:
#			return ''.join(value.split(','))
			return value.replace(',', '')
	# After read csv, I got a list, so need declare RootModel here
	class Root(RootModel):
		root:list[Stock]

	fpath:str = "個股日成交資訊.csv"
	stocks:list[dict] = get_csv_list(fpath)
	root:Root = Root.model_validate(stocks)
	print(root)
	stock_list = list(root)
	pprint(stock_list)


if '__main__' == __name__:
	practice1()
