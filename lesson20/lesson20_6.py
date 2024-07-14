import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	df1 = pd.read_csv(
		"2019~2023進出站人數.csv",
		index_col="日期",
		usecols=['日期', '車站名稱', '進站人數', '出站人數'],
		parse_dates=True
	)
	# Clear all indies and reassign index
	# 重新指定 index '日期' and '車站名稱'
	df2 = df1.reset_index(inplace=True).set_index(keys=['日期', '車站名稱'])
	show_df_part(df2)
	# columns 不是 multiple index，故只能用 name
	# TODO: 這裡 DataFrame 的 columns 又指定名稱 name 的作用為何？
	# columns.name 好像是 columns 的代名，就當成是 columns 的 level name 吧
	df2.columns.name = '人數'
	print(f"df2.columns type: {type(df2.columns.name)}")
	print(f"df2.columns.name type: {type(df2.columns.name)}")
	#pprint(df2['進站人數'])
	df2.info()
	show_df_part(df2)
	# stack level 為人數，傳回的 series 會把 '進站人數' 和 '出站人數' 從 column 轉到 row，
	# 且此 row 的 column 為 '人數'
	s1 = df2.stack(level='人數')
	# stack level 指定 columns 或出錯
#	s1 = df2.stack(level=['進站人數', '出站人數'])
	pprint(s1)
	# s1.index.levels 是 list 的 list，所以必須指定 list index 才能取出資料
	pprint(s1.index.levels)		# list of list
	pprint(s1.index.levels[0])	# get first list of parent list

	print("\ns1 reset index 後，新的 DataFrame 有進出站人數的欄位，但沒有欄位名稱")
	print(f"s1 type {type(s1)}")
	# Series reset_index() - Generate a new DataFrame or Series with the index reset.
	df3 = s1.reset_index(inplace=True)
	print(f"df3 type {type(df3)}")
	# 重新命名欄位名稱，最後一欄原為 0，現更名為 '數量'
	print("\n重新命名欄位名稱，最後一欄原為 0，現更名為 '數量'")
	df3.columns = ['日期','車站名稱','人數','數量']
	show_df_part(df3)
	print(df3.columns)

	print("\n處理日期")
	year_series = df3['日期'].dt.year
	print(type(year_series))
	pprint(year_series)
	#pprint(year_series.keys)
	pprint(year_series.values)

	pprint(s1.groupby(by=year_series.values))
	# 只能取得年度總進出人數，無法做詳細分析
	pprint(s1.groupby(by=year_series.values).sum())
	#pprint(s1.groupby(by=[year_series.values, df3['車站名稱'], df3['人數']]).sum())

#	# 重新命名欄位名稱，最後一欄原為 0，現更名為 '數量'
#	print("\n重新命名欄位名稱，最後一欄原為 0，現更名為 '數量'")
#	df3.columns = ['日期','車站名稱','人數','數量']
#	show_df_part(df3)
	pprint(df3['數量'].groupby(by=[year_series.values, df3['車站名稱'], df3['人數']]).sum())

	#pprint(s1.groupby(level='日期'))
	#pprint(s1.groupby(level=['日期', '人數']).sum())


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
