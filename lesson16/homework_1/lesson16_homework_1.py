import pandas as pd
from tabulate import tabulate

def number_add_comma(val):
	# 傳入的 val 的 data type 始終為 str (原因待查)
	# 故強制轉換 val 的 data type 為 int 或 float
	# 若出現 exception 則傳回 -1
	try:
		val_dtype = type(val)
		if val_dtype == str:
			_val = float(val) if '.' in val else int(val)
		else:
			_val = val
		return "{:,}".format(_val)
	except Exception as e:
		print(e)
		return "-1"

def _main():
	csv_file:str = "上市公司資料.csv"
	# 依需求轉換公司代號為字串
	dtype_map:dict = {
		'公司代號': 'str',
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
	df_cnt:int = csv_df.size
	print(f"共有 {df_cnt} 筆資料")

	# 因為 terminal 輸出無法像 Jupyter notebook 般的美麗
	# 故用 tabulate 來美化輸出
	print("\n最前五筆資料")
	print(tabulate(csv_df.head(5), headers="keys", tablefmt="simple"))
	# 練習用 head()， 功能同 print(tabulate(csv_df.iloc[:5,:]))
	print("\n最後五筆資料")
	# pandas.dataFrame.to_markdown() 是實作 tabulate 來的
	print(csv_df.tail(5).to_markdown())
	# 練習用 tail()， print(tabulate(csv_df.iloc[-5:,:]))

if __name__ == '__main__':
	_main()
