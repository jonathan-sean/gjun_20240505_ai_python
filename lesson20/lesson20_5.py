import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	df1 = pd.read_csv(
		"2019~2023進出站人數.csv",
		index_col="日期",
		usecols=['日期', '車站名稱', '進站人數', '出站人數']
	)
	# Clear all indies and reassign index
	df2 = df1.reset_index().set_index(keys=['日期', '車站名稱'])
	show_df_part(df2)
	# columns 不是 multiple index，故只能用 name
	df2.columns.name = '人數'
	show_df_part(df2)
	s1 = df2.stack(level='人數')
	pprint(s1)

	s2 = s1['2019-04-23':'2019-04-30']
	pprint(s2)

	# sum() 只處理能運算的 int 等 type，其他無法運算者會被 ignore
	print(s2.groupby(level=['日期']).sum())
	print("\ngroup by 日期 & 人數")
	print(s2.groupby(level=['日期', '人數']).sum())
	print("\ngroup by 人數 & 車站名稱")
	print(s2.groupby(level=['車站名稱', '人數']).sum())
	print("\nunstack by 人數")
	#print(type(s2.groupby(level=['車站名稱', '人數']).sum().unstack(level='人數')))
	print(s2.groupby(level=['車站名稱', '人數']).sum().unstack(level='人數'))

def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
