# Same with lesson19_1.py, but use my merge function
import pandas as pd
from MyPackage.myDisp import *
import json
from pprint import pprint

def _merge(fname:str, stations_name:pd.DataFrame):
	df1 = pd.read_csv(fname)
	col_map = {
		'trnOpDate': '日期',
		'staCode': '車站代碼',
		'gateInComingCnt': '進站人數',
		'gateOutGoingCnt': '出站人數',
	}
	df2 = df1.rename(columns=col_map)
	df2['日期'] = pd.to_datetime(df2['日期'].astype(str))
	return pd.merge(df2, stations_name, left_on='車站代碼', right_on='編碼', how='left')

def _practice_1():
	# 先取得車站基本資料，這是通用、不太會變動的資料，例如車站名稱、地址等
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

	# 整合二筆從不同來源的臺鐵車站資料
	# 每日各站進出站人數是變動的
	df = _merge("每日各站進出站人數2021.csv", stations_name)
	df.info()
	show_df_part(df, title='整合後的資料')

	fdir = os.path.dirname(os.path.realpath('每日各站進出站人數2021.csv'))
	fname_lst = os.listdir(fdir)
	abs_names = [os.path.join(fdir, n) for n in list(filter(lambda name: '每日各站進出站人數' in name, fname_lst))]
	pprint(abs_names)
	all_data = [_merge(abs_n, stations_name) for abs_n in abs_names]
	#pprint(all_data)
#	result = pd.concat(all_data, ignore_index=True)
	result = pd.concat(all_data).set_index('日期').sort_index()
	show_df_part(result, title="After Pandas concat()")
	result.info()
	result_2 = result.reindex(columns=['車站名稱', '地址', '進站人數', '出站人數'])
	show_df_part(result_2, title="After reindex")
	result_2.info()
	# Store result to CSV file
	result_2.to_csv("2019~2023進出站人數.csv")

def _practice_2():
	curr_dir = os.path.dirname(os.path.abspath(__name__))
	print(curr_dir)
	pprint(os.listdir(curr_dir))
	#fname = os.path.realpath(os.path.join(curr_dir, '每日各站進出站人數2021.csv'))
	fname = os.path.realpath('每日各站進出站人數2021.csv')
	print(f"real path: {fname}")
	fdir = os.path.dirname(fname)
	print(fdir)
	fname_lst = os.listdir(fdir)
	pprint(fname_lst)
	filter_names = list(filter(lambda name: '每日各站進出站人數' in name, fname_lst))
	pprint(filter_names)
	abs_names = [os.path.join(fdir, n) for n in filter_names]
	pprint(abs_names)

def _main():
	_practice_1()
#	_practice_2()

if __name__ == "__main__":
	_main()
