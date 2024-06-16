# 下載台北市youbike及時資料(json),解析資料
#  - URL: https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
#  - 查出目前可借車輛數為3輛以內的站點
#  - 查出目前可還車輛數為3輛以內的站點
#  - 將維護的站點移除

import traceback
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
import pyinputplus as pyip
from random import choices

# Inherited from PyDantic BaseModel
class UBike(BaseModel):
	act:bool
	mday:str
	sarea:str
	sna:str
	ar:str
	latitude:float
	longitude:float
	available_rent_bikes:int
	available_return_bikes:int
	total:int
# Inherited from PyDantic RootModel
class UBikeRoot(RootModel):
	root:list[UBike]

# Return True if each pattern matched
def _filter_bike_any(item:dict, patterns:list[dict]) -> bool:
	for (k, v) in patterns.items():
		if item[k] <= v:
			return True
	return False

# Return True if all patterns matched
def _filter_bike_all(item:dict, patterns:list[dict]) -> bool:
	for (k, v) in patterns.items():
		if item[k] > v:
			return False
	return True

def main():
	title:str = "臺北市 U-Bike 即時資訊"
	try:
		youbike_url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
		resp:Response = requests.get(youbike_url)
		if not resp.ok:
			print(f"ERROR: 下載{title}失敗")
			return
		resp.close()

		# This JSON include integer and float, but python json module cannot parse these data
		# How to correct these ?
		# Load generic text and call model_validate() to get data in required fields
		data:UBikeRoot= UBikeRoot.model_validate(json.loads(resp.text))
		# convert UBikeRoot to dictionary list by model_dump()
		data_dlst_full:list[dict] = data.model_dump()

		# filter data
		# First filter activate
		act:bool = True
		data_dlst_act:list[dict] = list(filter(lambda item:item['act'] == act, data_dlst_full))

		# For my practice
		# Try to use a dictionary to store search criteria
		patterns:dict[str: int] = { "available_rent_bikes": 3, "available_return_bikes": 3 }
		# Use the special lambda function approach
		data_dlst_filtered:list[dict] = list(filter(lambda item:_filter_bike_any(item, patterns), data_dlst_act))

		print(f"{title}：")
		print(f"全部有 {len(data_dlst_full)} 筆資料")
		print("\n搜尋")
		print(str.format("\t- {}", '營運中' if act else '休息中'))
		print(str.format("\t- 可借車輛數: {} 輛(含)以內", patterns['available_rent_bikes']))
		print(str.format("\t- 可還車輛數: {} 輛(含)以內", patterns['available_return_bikes']))
		cnt = len(data_dlst_filtered)
		print(f"\t共有 {cnt} 筆符合條件的資料")
		if cnt == 0:
			return
		# Sort by mday
		n = pyip.inputInt(f"\n請輸入要隨機顯示的資料數(1~{cnt}): ", min=1, max=cnt)
		sort_key:str = 'mday'
		data_dlst_filtered:list[dict] = sorted(choices(data_dlst_filtered, k=n), key=lambda item: item[sort_key], reverse=True)
		i:int = 0
		for d in list(data_dlst_filtered):
			i += 1
			print(f"第 {i} 筆")
#			print(str.format("Index: {}", data_dlst_full.index(d)))
			#pprint(d, indent=2)
			for (k, v) in d.items():
				print(f"\t{k}: {v}")
	except Exception as e:
		print(f"EXCEPTION: {e}")
		traceback.print_exc()


if '__main__' == __name__:
	main()
