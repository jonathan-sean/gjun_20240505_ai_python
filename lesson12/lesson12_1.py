import json
from pprint import pprint

def practice1():
	# Declare classes to parse JSON data through the PyDantic
	from pydantic import (
		BaseModel,
		Field,
		ValidationError,
		field_validator
	)
	# For specific JSON data
	class Record(BaseModel):
		site:str = Field(alias='sitename')
		county:str
		aqi:str
		status:str
		pm25:float = Field(alias='pm2.5')
		@field_validator("pm25", mode="before")
		@classmethod
		# In field_validator, the first parameter of its method cannot set 'self', must set 'cls'
		# If set 'self' will get exception <class 'pydantic.errors.PydanticUserError'> - `@field_validator` cannot be applied to instance methods
		# Because the validator method is a class method, not a instance method
		# Refer to https://errors.pydantic.dev/2.7/u/validator-instance-method
		#def pm25_to_zero(self, value:str)->str:
		def pm25_default_zero(cls, value:str)->str:
			if value == '':
				return '0.0'
			return value
	# For complete JSON data
	# JSON default is dictionary type, so declare BaseModel here
	class Root(BaseModel):
		records:list[Record]
	def filter_pm25(item:dict) -> bool:
		return(item['pm25'] == 0.0)

	try:
		# Read JSON file
		fpath:str = "aqx_p_488.json"
		fname:str = fpath.removesuffix(".csv")
		print(f"[practice1] JSON: {fname}")
		with open(fpath, encoding='UTF-8') as f:
			json_content:str = f.read()

		# Fetch complete JSON data
		aqi:Root = Root.model_validate_json(json_content)
		#print(aqi)
		#print(type(aqi))
		# Convert JSON format to Python dictionary list
		data_dict:dict = aqi.model_dump()
		data_dlst:list[dict] = data_dict['records']
		print(str.format("Complete data has {} records", len(data_dlst)))
#		for d in data_dlst:
#			print(d)
		data_dlst_nopm25:list[dict] = list(filter(filter_pm25, data_dlst))
		print(str.format("Data's PM2.5 is zero which has {} records", len(data_dlst_nopm25)))
		# Use lambda function
		data_dlst_haspm25:list[dict] = list(filter(lambda d: d['pm25'] != 0.0, data_dlst))
		print(str.format("Data filter out zero PM2.5 has {} records", len(data_dlst_haspm25)))
		sort_key:str = 'pm25'
		data_dlst_haspm25_sorted:list[dict] = sorted(data_dlst_haspm25, key=lambda i: i[sort_key])
		#pprint(data_dlst_haspm25_sorted)
#		pprint(data_dlst_haspm25_sorted[:5])
		pprint(data_dlst_haspm25_sorted[-10:0])
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")

def practice2():
	# filter data of list
	numbers:list[int] = [1,2,10,4,7,5,6,3,8,9,]
	def is_even(num:int) -> bool:
#		if num % 2 == 0:
#			return True
#		return False
		return num % 2 == 0
	def is_odd(num:int) -> bool|None:
#		if num % 2 != 0:
#			return True
#		return True if num % 2 != 0 else False
		return num % 2 != 0
	print(str.format("Even: {}", list(filter(is_even, numbers))))
	print(str.format("Odd: {}", list(filter(is_odd, numbers))))
	# Use lambda function instead of general function
	print(str.format("Use lambda - Even: {}", list(filter(lambda num: num %2 == 0, numbers))))
	print(str.format("Use lambda - Odd: {}", list(filter(lambda num: num %2 != 0, numbers))))
	print(str.format("sorted: {}", sorted(numbers)))
	print(str.format("Reverse sorted: {}", sorted(numbers, reverse=True)))


if "__main__" == __name__:
	try:
		practice1()
#		practice2()
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")
