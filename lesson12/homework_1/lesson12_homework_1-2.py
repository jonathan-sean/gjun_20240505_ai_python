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
	rents:int = Field(alias="available_rent_bikes")
	returns:int = Field(alias="available_return_bikes")
	total:int

# Inherited from PyDantic RootModel
class UBikeRoot(RootModel):
	root:list[UBike]

def _search_bike(dlist:list[dict], key:str, val_min:float=1, val_max:float=1, sort:bool=False, sort_key:str='mday', reverse=True):
	_dlst:list[dict] = list(filter(lambda item:item[key] >= val_min and item[key] <= val_max, dlist))
	if sort:
		_dlst = sorted(_dlst, key=lambda item: item[sort_key], reverse=reverse)
	return _dlst

# Return True if each pattern matched
def _search_bike_any(item:dict, patterns:list[dict]) -> bool:
	for (k, v) in patterns.items():
		if item[k] > 0 and item[k] <= v:
			return True
	return False

# Return True if all patterns matched
def _search_bike_all(item:dict, patterns:list[dict]) -> bool:
	for (k, v) in patterns.items():
		if item[k] <= 0 or item[k] > v:
			return False
	return True

def _display_sites_random(dlist:list[dict], sort:bool=True, sort_key:str='mday', reverse=True):
	max:int = len(dlist)
	if max == 0:
		return None
	try:
		n:int = pyip.inputInt(f"請輸入要隨機顯示的站點(1~{max}): ", min=1, max=max)
		dlst_random:list[dict] = choices(dlist, k=n)
		if sort:
			dlst_random = sorted(dlst_random, key=lambda item: item[sort_key], reverse=reverse)
		i:int = 0
		for d in list(dlst_random):
			i += 1
			print(f"第 {i} 筆")
			for (k, v) in d.items():
				print(f"\t{k}: {v}")
	except Exception as e:
		raise e

def main():
	title:str = "臺北市 U-Bike 即時資訊"
	try:
		ubike_url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
		resp:Response = requests.get(ubike_url)
		if not resp.ok:
			print(f"ERROR: 下載{title}失敗")
			return
		resp.close()

		# This JSON include integer and float, but python json module cannot parse these data
		# How to correct these ?
		# Load generic text and call model_validate() to get data in required fields
		jaon_raw:UBikeRoot= UBikeRoot.model_validate(json.loads(resp.text))
		# convert UBikeRoot to dictionary list by model_dump()
		ubike_full:list[dict] = jaon_raw.model_dump()
		print(f"{title}：")
		print(f"全部有 {len(ubike_full)} 個 U-Bike 站點")

		# filter data
		#  1.Search for active sites
		act:bool = True
		ubike_act:list[dict] = list(filter(lambda item:item['act'] == act, ubike_full))

		patterns:dict[str: int] = { "rents": 3, "returns": 3 }
		display_mode:int = 1	# default display or condition
		if display_mode == 1:
			#  2. Search for bikes to rent
			key:str = "rents"
			#ubike_lst:list[dict] = list(filter(lambda item:item[k] > 0 and item[k] <= n, ubike_act))
			ubike_lst:list[dict] = _search_bike(ubike_act, key, val_max=patterns[key])
			print(str.format("\n營運中且可借車輛數在 {} 輛(含)以內的有站點 {} 個", patterns[key], len(ubike_lst)))
			_display_sites_random(ubike_lst, sort_key=key)

			#  3. Search for bikes to return
			key = "returns"
			#ubike_lst:list[dict] = list(filter(lambda item:item[k] > 0 and item[k] <= n, ubike_act))
			ubike_lst:list[dict] = _search_bike(ubike_act, key, val_max=patterns[key])
			print(str.format("\n營運中且可還車輛數在 {} 輛(含)以內的站點有 {} 個", patterns[key], len(ubike_lst)))
			_display_sites_random(ubike_lst, sort_key=key)
		else:
			#  2. Search available rental and return bikes using or criteria
			# For my practice
			# Try to use a dictionary to store search criteria
			# For functions with more parameters, use the special lambda function approach
			ubike_lst:list[dict] = list(filter(lambda item:_search_bike_any(item, patterns), ubike_act))
			print("\n搜尋")
			print(str.format("\t- {}", '營運中' if act else '休息中'))
			print(str.format("\t- 可借車輛數: {} 輛(含)以內", patterns['rents']))
			print(str.format("\t- 可還車輛數: {} 輛(含)以內", patterns['returns']))
			cnt:int = len(ubike_lst)
			print(f"\t共有 {cnt} 個符合條件的站點")
			_display_sites_random(ubike_lst)
	except Exception as e:
		print(f"EXCEPTION: {e}")
		traceback.print_exc()


if '__main__' == __name__:
	main()
