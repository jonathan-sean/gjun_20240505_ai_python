import pandas as pd
from MyPackage.myDisp import *
import json
from pprint import pprint

def _practice_1():
	# 整合二筆從不同來源的臺鐵車站資料
	df1 = pd.read_csv("每日各站進出站人數2020.csv")
	col_map = {
		'trnOpDate': '日期',
		'staCode': '車站代碼',
		'gateInComingCnt': '進站人數',
		'gateOutGoingCnt': '出站人數',
	}
	df2 = df1.rename(columns=col_map)
	df2.info()
	show_df_part(df2)
	df2['日期'] = pd.to_datetime(df2['日期'].astype(str))
	df2.info()
	show_df_part(df2)

	with open('車站基本資料集.json', encoding='utf-8') as f:
		json_data = json.load(f)
	#pprint(json_data)
	col_map = {
		"stationCode": "編碼",
		"stationName": "車站名稱",
		"stationAddrTw": "地址",
	}
	stations_name = pd.DataFrame(json_data, columns=col_map.keys()).rename(columns=col_map)
	# 要將 '編碼' 轉為 int type
	stations_name['編碼'] = stations_name['編碼'].astype(int)
	stations_name.info()
	show_df_part(stations_name)


	# how:
	#  inner: 交集
	#  outer: 聯集
	# NOTE: merge 時，left_on 和 right_on 的 data type 必須一致
	result_df = pd.merge(df2, stations_name, left_on='車站代碼', right_on='編碼', how='left')
	result_df.info()
	show_df_part(result_df, title='整合後的資料')


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
