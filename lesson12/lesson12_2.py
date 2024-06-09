import json
from pprint import pprint
from pydantic import (
	BaseModel,
	RootModel,
	Field,
	ValidationError,
	field_validator
)

def get_json_data(fpath:str) -> dict:
	with open(fpath, encoding='UTF-8') as f:
		json_content:str = f.read()
		data_dict:list[dict] = json.loads(json_content)
	return data_dict

def get_json_data_2(fpath:str) -> dict:
	with open(fpath, encoding='UTF-8') as f:
		data_dict:list[dict] = json.load(f)
	return data_dict

def practice1():
	try:
		fpath:str = "aqx_p_488.json"
		fname:str = fpath.removesuffix(".csv")
		print(f"[practice1] JSON: {fname}")
		with open(fpath, encoding='UTF-8') as f:
			json_content:str = f.read()
			data_dlst:list[dict] = json.loads(json_content)
		print(data_dlst)
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")

def practice2():
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
	# For dictionary list
	class Root(RootModel):
		root:list[Record]

	try:
		fpath:str = "aqx_p_488.json"
		fname:str = fpath.removesuffix(".csv")
		print(f"[practice2] JSON: {fname}")
		data_all:dict = get_json_data_2(fpath)
		# Remember convert dictionary to list that contain required data in 'records'
		record_dlst = list(data_all['records'])
#		pprint(record_dlst)
		root:Root=  Root.model_validate(record_dlst)
		print(root)
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")



if "__main__" == __name__:
	try:
#		practice1()
		practice2()
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")
