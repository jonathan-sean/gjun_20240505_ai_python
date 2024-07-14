import numpy as np
import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
					'key2':['one', 'two', 'one', 'two', 'one'],
					'data1': np.random.randint(1,11,size=5),
					'data2':np.random.randint(1,11,size=5)})
	show_df_all(df)
	# 直接從 DataFrame 解析資料
	print(type(df.groupby(by=['key1', 'key2'])))
	pprint(df.groupby(by=['key1', 'key2']).sum())
	#print(type(df.groupby(by=['key1', 'key2']))['data1'])
	pprint(df.groupby(by=['key1', 'key2'])['data1'].sum())

def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
