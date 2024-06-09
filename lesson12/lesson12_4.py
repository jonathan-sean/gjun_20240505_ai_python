import json
import requests
from requests import Response
from pprint import pprint
from pydantic import (
	BaseModel,
	RootModel,
	Field,
	ValidationError,
	field_validator
)

def practice1():
	class UBike(BaseModel):
		sna:str
		sarea:str
		mday:str
		ar:str
		act:int
		total:int
		latitude:float
		longitude:float
		available_rent_bikes:int
		available_return_bikes:int
	class UBikeRoot(RootModel):
		root:list[UBike]

	try:
		youbike_url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
		resp:Response = requests.get(youbike_url)
		if resp.ok:
			print("Download success.")
		else:
			print("Download fail.")

	#	pprint(resp.text)
		resp_json:list[dict] = json.loads(resp.text)
		print(type(resp_json))
		print(len(resp_json))
#		pprint(resp_json)
#		for d in list(resp_json):
#			pprint(d)
#		json.loads(resp_json, parse_int=str, parse_float=str)
#		data_full:UBikeData = UBikeData.model_validate_json(resp_json)
		# This JSON include integer and float, but python json module cannot parse these data
		# How to correct these ?
		# Call model_validate() to get data in required fields
		data_full:UBikeRoot = UBikeRoot.model_validate(resp_json)
		if False:
			print("\nAfter model_dump_json")
			# model_dump_json() return JSON string, so call json.loads() again
			data_json:list[dict] = json.loads(data_full.model_dump_json())
			print(type(data_json))
			print(len(data_json))
			pprint(data_json[:5])

			print("\nAfter model_dump")
			data_dlst:list[dict] = data_full.model_dump()
			pprint(type(data_dlst))
			pprint(data_dlst[:5])
			pprint(len(data_dlst))
	#		for d in list(data):
	#			pprint(d)

		# filter data
		#keys:str[] = [ "act", "available_rent_bikes", "available_return_bikes" ]
	except Exception as e:
		print(f"EXCEPTION: {e}")


if '__main__' == __name__:
	practice1()
