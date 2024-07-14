import numpy as np
import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
					'key2':['one', 'two', 'one', 'two', 'one'],
					'data1': np.random.randint(1,11,size=5),
					'data2':np.random.randint(1,11,size=5)})
	show_df_all(df)
	# df['data1'].groupby(df['key1']) will return a SeriesGroupBy object
	pprint(df['data1'].groupby(df['key1']).sum())
	pprint(df['data1'].groupby(by=[df['key1'], df['key2']]).count())
	print(df['data1'].groupby(['台北','台北','台北','台中','台中']).count())

	print(type(df[['data1', 'data1']]))
	show_df_all(df[['data1', 'data1']])
	print(type(df[['data1', 'data1']].groupby(by=[df['key1'],df['key2']])))
	show_df_all(df[['data1', 'data1']].groupby(by=[df['key1'],df['key2']]).sum())

def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
