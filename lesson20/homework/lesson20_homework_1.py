# 將各鄉鎮市區人口密度資料夾內的csv檔,清理資料後,組成全新的DataFrame
import os
import pandas as pd

#----------------------------------------------------------
# For store result to HTML file
#----------------------------------------------------------
def _float_format(v):
	return "{:.2f}".format(v)

# _export_to_html_part
# 把部分 Pandas DataFrame 資料寫入 HTML file
def _export_to_html_part(data:pd.DataFrame, title:str=None, first:int=5, last:int=5, append:bool=True):
	mode = 'a' if append else 'w'
	fpath = os.path.basename(__file__).replace('py', 'html')
	with open(fpath, mode) as f:
		# Check for add title
		if title:
			f.write(title)
		# Check for add head data
		if first > 0:
			f.write(data.iloc[:first,:].to_html(float_format=_float_format))
			f.write(".....")
		f.write(data.iloc[-last:,:].to_html(float_format=_float_format))
		f.write("<br>")

# _export_to_html_all
# 把所有 Pandas DataFrame 資料寫入 HTML file
def _export_to_html_all(data:pd.DataFrame, title:str=None, append:bool=True):
	_export_to_html_part(data, title=title, first=0, last=0, append=append)
#----------------------------------------------------------


def _process_data(fname:str, path:str):
	# 指定 header=1 從第二列開始取資料並去除 NaN 資料
	df = pd.read_csv(os.path.join(path, fname), header=1).dropna()
#	# 去除無法轉換成數值的人口資料
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
	return df

def _main():
	data_path:str = "各鄉鎮市區人口密度"
	abs_path:str = os.path.abspath(data_path)
	all_data = [_process_data(f, abs_path) for f in os.listdir(abs_path)]
	# 整合資料並依年底人口數排序
	result = pd.concat(all_data).set_index('統計年')
	result.sort_values('年底人口數', ascending=False, inplace=True)
	_export_to_html_part(result, title="依年底人口數排序列出部分資料", append=False)

if __name__ == "__main__":
	_main()
