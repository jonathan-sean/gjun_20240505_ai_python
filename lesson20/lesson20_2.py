import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	df1 = pd.read_csv(
		"2019~2023進出站人數.csv",
		index_col="日期",
		usecols=['日期', '車站名稱', '進站人數', '出站人數']
	)
	show_df_part(df1)
	show_df_all(df1[:20])
	df1.info()
	show_df_part(df1.loc['2019-04-23'])
	show_df_part(df1.loc['2019-04-20':'2019-04-30'])
	show_df_part(df1.loc['2020-03':'2020-05'])

	# Clear all indies and reassign index
	df2 = df1.reset_index().set_index(keys=['日期', '車站名稱'])
	show_df_part(df2)

	# columns 不是 multiple index，故只能用 name
	df2.columns.name = '人數'
	show_df_part(df2)
	s1 = df2.stack(level='人數')
	pprint(s1)
	# Below line will fail, why?
	#pprint(df2.stack(level='車站名稱'))
	# Below line will fail, why?
	#pprint(df2.unstack(level='人數'))
	s1 = s1.unstack(level='車站名稱')
	pprint(s1)

	s2 = s1['2019-04-23':'2019-04-30']
	pprint(s2)

	# groupby: 集合相同欄位名稱的資料
	#pprint(s2.groupby(level='車站名稱').sum())
	pprint(s2.groupby(level=['車站名稱','人數']).sum())


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
