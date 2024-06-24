import pandas as pd
#from IPython.display import display
from tabulate import tabulate
import pyinputplus as pyip
from random import choices

def int_to_str(val:int, comma=True):
	#print(f"val type: {type(val)}")
	if comma:
		return "{:,}".format(int(val))
		#return str.format(",d", val)
		#return "{:,}".format(val)
	return val

def set_pandas_display_options():
	# Ref: https://stackoverflow.com/a/52432757/
	display = pd.options.display

#	display.max_columns = 1000
	display.max_rows = 10
#	display.max_colwidth = 199
	display.width = None
	# display.precision = 2  # set as needed
	display.colheader_justify = 'center'

def number_add_comma(val):
	# 傳入的 val 的 data type 始終為 str (原因待查)
	# 故強制轉換 val 的 data type 為 int 或 float
	# 若出現 exception 則傳回 -1
	#	print(f"val type: {type(val)}")
	try:
		val_dtype = type(val)
		if val_dtype == str:
			_val = float(val) if '.' in val else int(val)
			#if '.' in val:
			#	return "{:,.2f}".format(float(val))
			#_val = int(val)
		else:
			_val = val
		#print(f"_val type: {type(_val)}")
		return "{:,}".format(_val)
	except Exception as e:
		print(e)
		return "-1"

def _display_records_random(dlist:list[dict], sort:bool=True, sort_key:str='mday', reverse=True):
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

def _main():
	csv_file:str = "上市公司資料.csv"
	# 依需求轉換公司代號為字串
	dtype_map:dict = {
		'公司代號': 'str',
#		'營業收入-當月營收': 'str',
#		'營業收入-上月營收': 'str'
	}
	# 依需求轉換營業收入為含逗號的字串
	conv_map:dict = {
		'營業收入-當月營收': number_add_comma,
		'營業收入-上月營收': number_add_comma
	}
	csv_df:pd.DataFrame = pd.read_csv(
		csv_file,
		# 指定公司名稱為 index
		index_col=['公司名稱'],
		# 指定要顯示的欄位
		usecols=['公司代號', '公司名稱', '產業別', '營業收入-當月營收', '營業收入-上月營收'],
		dtype=dtype_map,
		converters=conv_map)
	#	thousands=",")
	df_cnt:int = csv_df.size
	print(f"共有 {df_cnt} 筆資料")
	#n:int = pyip.inputInt(f"請輸入要隨機顯示的資料(1~{df_cnt}): ", min=1, max=df_cnt)
	#df_random:list[dict] = choices(csv_df.to_numpy(), k=n)
	# 因為 terminal 輸出無法像 Jupyter notebook 般的美麗
	# 故用 tabulate 來美化輸出
	#print(pd.DataFrame(df_random,))
	print("\n最前五筆資料")
#	print(csv_df.head(5).to_markdown())
	print(tabulate(csv_df.head(5), headers="keys", tablefmt="simple"))
	# 練習用 head()， 功能同 print(tabulate(csv_df.iloc[:5,:]))
#	print(tabulate(csv_df.iloc[:5,:]))
	print("\n最後五筆資料")
	# pandas.dataFrame.to_markdown() 是實作 tabulate 來的
	print(csv_df.tail(5).to_markdown())
	# 練習用 tail()， print(tabulate(csv_df.iloc[-5:,:]))
#	print(tabulate(csv_df.tail(5), tablefmt="markdown"))
#	print(tabulate(csv_df.iloc[-5:,:]))
	#print(csv_df.to_markdown())
	#csv_df.style.background_gradient()
	#set_pandas_display_options()
	#display(csv_df.to_parquet())
	#csv_df.info()

def _test():
	# Python3 code to demonstrate working of
	# Adding comma between numbers
	# Using str.format()

	# initializing number
	test_num = 1234567

	# printing original number
	print("The original number is : " + str(test_num))

	# Using str.format()
	# Adding comma between numbers
	print(type(test_num))
	#res = '{:,}'.format(test_num)
	res = number_add_comma(test_num)
	print(type(res))

	# printing result
	print("The number after inserting commas : " + res)


if __name__ == '__main__':
	#_main()
	_test()
