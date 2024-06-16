import traceback
import requests
import json
from pydantic import (
	BaseModel,
	RootModel,
	Field,
	ValidationError,
	field_validator
)
from pprint import pprint

class UBike(BaseModel):
	act:bool
	mday:str
	sarea:str
	sna:str
	ar:str
	lat:float = Field(alias="latitude")
	lon:float = Field(alias="longitude")
	rents:int = Field(alias="available_rent_bikes")
	returns:int = Field(alias="available_return_bikes")
	total:int

class UBikeRoot(RootModel):
	root:list[UBike]

def practice_1():
	students = [("Alias", 25), ("Tom", 40), ("Hank", 15)]
	print(str.format("{}", sorted(students, key=lambda item:item[1])))
	print(str.format("{}", sorted(students, key=lambda item:item[1], reverse=True)))

def main():
	try:
		ubike_url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
		resp:Response = requests.request('GET', ubike_url)
		resp.raise_for_status()

		resp.close()
		datas:UBikeRoot = UBikeRoot.model_validate_json(resp.text)
		ubikes = datas.model_dump()
		#pprint(ubikes)
		print(str.format("total: {} records", len(ubikes)))
		#practice_1()
		ubikes_act = list(filter(lambda item: item['act'], ubikes))
		print(str.format("active: {} records", len(ubikes_act)))
		ubikes_sort_rents = sorted(ubikes_act, key=lambda item:item['rents'])
		#print("可借最少前五")
		#pprint(ubikes_sort_rents[:5])
		#print("可借最多前五")
		#pprint(ubikes_sort_rents[-5:])
		ubikes_rents_3 = list(filter(lambda item:item['rents'] <= 3, ubikes_act))
		print(str.format("rents <= 3: {} records", len(ubikes_rents_3)))
		ubikes_rturns_3 = list(filter(lambda item:item['returns'] <= 3, ubikes_act))
		print(str.format("returns <= 3: {} records", len(ubikes_rturns_3)))
	except Exception as e:
		print(f"EXCEPTION: 連線失敗 - {e}")
		traceback.print_exc()
	#else:
		#print(f"{resp.text}\n{type(resp.text)}")
		#resp.close()
		#datas:UBikeRoot = UBikeRoot.model_validate(json.loads(resp.text))

"""
	try:
		ubike_url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
		resp:Response = requests.request('GET', ubike_url)
		resp.raise_for_status()
	except Exception as e:
		print(f"EXCEPTION: {e}")
		traceback.print_exc()
"""


if __name__ == "__main__":
	main()
