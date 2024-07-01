# 台積電,聯電,聯發科,鴻海,2024年,(平均,中位數,最高價,最低價,最高價日期,最低價的日期)
from MyPackage import *
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import datetime, date



# 給擷取最高最低價資料時，維持 column 順序用
ticker_name:list = []

# _index_date_list
# 1. 從 DataFrame index 取得日期
# 2. 調整日期格式為 ISO format(%Y-%m-%d)
# Input:
#   1. df: Pandas DataFrame
# Return: date list
def _index_date_list(df:pd.DataFrame) -> list:
	lst:list = []
	for d in df.index:
#		print(d.date)
		#lst.append(f"{d.year}-{d.month}-{d.day}")
		lst.append(d.date().isoformat())
#	print(f"lst: {lst}")
	return lst

def _modify_date_fmt(df:pd.DataFrame):
	for i in df.index:
		if not isinstance(i, pd.Timestamp):
			continue
		print(f"{i}: type({type(i)})")
		print(i.date().isoformat())
		i.strftime("%Y-%m-%d")

# _parse_data
# 1. 解析出平均價, 中位數, 最高價, 最低價, 最高價日期和最低價日期資訊
# 2. 列出所有的最高價日期和最低價日期，用逗號區隔
# Input:
#   1. data: Pandas DataFrame
# Return: Pandas series data
def _parse_data(data:pd.DataFrame) -> pd.Series:
	max_price = data.max()
#	print("max_price: \n{}".format(max_price))
#	print("data[data == max_price]: {}\n{}".format(type(data[data == max_price]), data[data == max_price]))
#	print("data[data == max_price].index: \n{}".format(data[data == max_price].index))
#	df_max = data[data == max_price]
#	print("df_max.index: \n{}".format(df_max.index))
#	print("df_max.index.tolist(): \n{}".format(df_max.index.tolist()))
	#print("df_max.index.tolist().date(): \n{}".format(df_max.index.tolist().date()))
	max_date = ",".join(_index_date_list(data[data == max_price]))
	#max_date = df_max.index.tolist()[0]
#	print(f"max_date: \n{max_date}")
	min_price = data.min()
#	df_min = data[data == min_price]
#	min_date = data[data == min_price].index.tolist()[0]
	min_date = ",".join(_index_date_list(data[data == min_price]))
#	print(f"min_date: \n{min_date}")
	mean = data.mean()
	median = data.median()
	return pd.Series(
		[mean, median, max_price, min_price, max_date, min_date],
		index=['平均', '中位數', '最高價', '最低價', '最高價日期', '最低價日期'])

# _get_for_date
# 依據指定的 date 來擷取 dataFrame
# Input
#   1. data: Pandas DataFrame
#   2. date_lst: expected date list
# Return: pd.DataFrame
def _get_for_date(data:pd.DataFrame, date_lst:list) -> pd.DataFrame:
	global ticker_name
	print("--------------------------------")
	print(date_lst)
	#print(data)
	#print(data.index)
	# add DataFrame 後會有 column 順序改變情形
	# 為維持 column 順序，create DataFrame 時指定 column 順序
	df_nu = pd.DataFrame(columns=ticker_name, copy=False)
#	df_nu = pd.DataFrame(copy=False)
	for idx in data.index.tolist():
		#print(i.date().isoformat())
		if idx.date().isoformat() in date_lst:
			#print(type(i))
			#print(f"v: {v}\ni: {i}")
			df = data[data.index == idx]
#            print(df)
#            print(type(df))
			df_nu = df_nu.add(df, fill_value=0)
			# 雖然 reference 說 add 等於 +，但實際有出入，以下方式內容為 None
#			df_nu = df_nu + df
			#v1 = v[v.index == i]
			#print(v1
			#print(type(v1))
	print(">>--------------------------------")
	return df_nu

def _main():
	global ticker_name
	# Set mapping table of ticker and ticker name
	ticker_map:dict = {'2330.TW':'臺積電', '2303.TW':'聯電', '2454.TW':'聯發科', '2317.TW':'鴻海'}
	# Generate ticker list from ticker name mapping table
	ticker_lst:list = ticker_map.keys()
#	ticker_lst = ['2330.TW', '2303.TW', '2454.TW', '2317.TW']
	print(ticker_lst)
	ticker_name = ticker_map.values()
	print(ticker_name)
	# 直接指定要擷取的資料年份，以減少資料大小和處理程序
	# Set the start and end date
	get_year = 2024
	start = date(get_year, 1, 1)
	end = date(get_year, 12, 31)
#	start = f"{get_year}-01-01"
#	end = f"{get_year}-12-31"
#	all_data = {ticker: pdr.DataReader(ticker, 'yahoo', start=start, end=end) for ticker in ticker_lst}
	# Get stock data from Yahoo
	# 注意: yfinance 和 pandas_datareader 的說明文件不甚詳盡，使用時要特別小心
	# NOTE: Don't forget call yf.pdr_override() first
	yf.pdr_override()
	all_data:dict = {ticker:pdr.get_data_yahoo(ticker, start=start, end=end) for ticker in ticker_lst}
	print(type(all_data))
#	show_df_part(all_data)
	# Convert stock data (dict) to Pandas DataFrame, change the column name and drop null data
	df_year:pd.DataFrame = pd.DataFrame({k:v['Adj Close'] for k,v in all_data.items()}, copy=False).rename(columns=ticker_map).dropna()
	df_year.info()
	# Search all data for expected year
#	df_year = df.loc[str(get_year)]
#	print(df_year.index)
#	df_year.index = df_year.index.apply((lambda _: datetime.strptime(_,"%Y-%m-%d")))
#	show_df_part(df_year)
#	show_df_part(df_year, fmt='md')
	show_df_part(df_year, title="2024 全年股票資料(共 {} 筆，僅顯示部分)".format(len(df_year)))
	df_parsed = df_year.apply(_parse_data)
	print(df_parsed.index)
	show_df_all(df_parsed, title="分析後的 2024 全年股票資訊")

	# 列出最高價和最低價的資料
	chk_lst:list = ['最高價', '最低價']
	for chk in chk_lst:
		# Generate date list
		date_lst:list = []
		chk_col:str = chk+'日期'
		for v in df_parsed.loc[chk_col].values:
			date_lst += v.split(',')
		df_chk = _get_for_date(df_year, date_lst)
		show_df_all(df_chk, title="{}資料有 {} 筆".format(chk, len(df_chk)))

	# 結合二組 DataFrame
	# NOTE: pd.concat() 結合後的 DataFrame index 會出現時間，與結合前不同
	# TODO: 需要調整結合後的 index 只有日期，不要時間
	df_combined = pd.concat([df_year, df_parsed])
#	df_combined = df_year.combine_first(df_parsed)
#	df_combined = df_year.merge(df_parsed)
	#print(df_combined.index)
	#_modify_date_fmt(df_combined)
	try:
		df_combined.index = pd.to_datetime(df_combined.index, format="%Y-%m-%d", errors='ignore')
	except Exception as e:
		pass
	show_df_part(df_combined, last=15)


if __name__ == "__main__":
	_main()
