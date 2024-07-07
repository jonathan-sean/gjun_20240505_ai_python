import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	df1 = pd.read_csv("每日各站進出站人數2020.csv")
	col_map = {
		'trnOpDate': '日期',
		'staCode': '車站代碼',
		'gateInComingCnt': '進站人數',
		'gateOutGoingCnt': '出戰人數',
	}
	df2 = df1.rename(columns=col_map)
	df2.info()
	show_df_part(df2)
	df2['日期'] = pd.to_datetime(df2['日期'].astype(str))
	df2.info()
	show_df_part(df2)


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
