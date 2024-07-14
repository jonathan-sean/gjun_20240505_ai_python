
from MyPackage.myDisp import *
import pandas as pd

def _process_data(fname:str, path:str):
	print(os.path.join(path, fname))
	# 指定 header=1 從第二列開始取資料並去除 NaN 資料
	df = pd.read_csv(os.path.join(path, fname), header=1).dropna()
	# 去除無法轉換成數值的人口資料
#	for s in ['…', '… ']:
#		idx_lst = df[ (df['年底人口數'] == s) | (df['人口密度'] == s)].index
#		df.drop(idx_lst, inplace=True)
	# 將人口資料的 '…' 轉為 0
	for s in ['…', '… ']:
		for k in ['年底人口數', '人口密度']:
			idx_lst = df[df[k] == s].index
			for i in idx_lst:
				for i in idx_lst:
					df.at[i, k] = '0'
	dtype_map:dict = {
		'統計年': int,
		'年底人口數': int,
		'土地面積': float,
		'人口密度': int,
	}
	df = df.astype(dtype_map, copy=False)
	df.sort_values('年底人口數', ascending=False, inplace=True)
	#show_df_part(df)
	df.info()
	return df

def _main():
	data_path:str = "各鄉鎮市區人口密度"
	abs_path:str = os.path.abspath(data_path)
	all_data = [_process_data(f, abs_path) for f in os.listdir(abs_path)]
	# 整合資料並依統計年排序
#	result = pd.concat(all_data).sort_values('統計年').sort_values(['年底人口數', '人口密度'], ascending=False)
#	result = pd.concat(all_data).sort_values('統計年').sort_values('年底人口數', ascending=False)
#	result = pd.concat(all_data).set_index(['統計年', '年底人口數']).sort_index()
	result = pd.concat(all_data).set_index('統計年')
	result.sort_values('年底人口數', ascending=False, inplace=True)
	show_df_part(result)

if __name__ == "__main__":
	_main()
