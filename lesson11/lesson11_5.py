import json
from pprint import pprint

def practice1():
	# Read JSON file
	fpath:str = "aqx_p_488.json"
	fname:str = fpath.removesuffix(".csv")
	print(f"[practice1] JSON: {fname}")
	with open(fpath, encoding='UTF-8') as f:
		json_content:str = f.read()

	# Declare classes to parse JSON data through the PyDantic
	from pydantic import BaseModel, Field, ValidationError, field_validator
	# For specific JSON data
	class Site(BaseModel):
		sitename:str
		county:str
		aqi:str
		pm25:int = Field(alias='pm2.5')
		@field_validator("pm25", mode="before")
		@classmethod
		# In field_validator, the first parameter of its method cannot set 'self', must set 'cls'
		# If set 'self' will get exception <class 'pydantic.errors.PydanticUserError'> - `@field_validator` cannot be applied to instance methods
		# Because the validator method is a class method, not a instance method
		# Refer to https://errors.pydantic.dev/2.7/u/validator-instance-method
		#def pm25_to_zero(self, value:str)->str:
		def pm25_default_zero(cls, value:str)->str:
			if value == '':
				return '0'
			return value
	# For complete JSON data
	class AQI(BaseModel):
		records:list[Site]

	try:
		# Fetch complete JSON data
		aqi:AQI = AQI.model_validate_json(json_content)
		print(aqi)
		print(type(aqi))
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")


if "__main__" == __name__:
	try:
		practice1()
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")
