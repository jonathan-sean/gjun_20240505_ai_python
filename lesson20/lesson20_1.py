import numpy as np
import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	midx = [
			['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
			['1', '2', '3', '1', '2', '3', '1', '2', '3'],
		]
	data = np.random.randn(9)
	s1 = pd.Series(data, index=midx)
	s1.index.names = ['key1','key2']
	pprint(s1)

	s2 = pd.Series(
			data,
			index=pd.MultiIndex.from_arrays(midx, names=['key1', 'key2'])
		)
	pprint(s2)

	print("\nTransfer stack data to non-stack")
	show_df_all(s2.unstack(level='key1', fill_value=0))
	show_df_all(s2.unstack(level='key2', fill_value=0))
	s3 = s2.unstack(level='key1', fill_value=0)
	show_df_all(s3.T)
	show_df_all(s3.T.T)

def _practice_2():
	frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
						index=pd.MultiIndex.from_arrays([['a','a','b','b'],[1, 2, 1, 2]],names=['key1','key2']),
						columns=[['台北','台北','台中'],['Green','Red','Green']])
	frame.columns.names = ['縣市','顏色']
	show_df_all(frame, title='All frame data')
	show_df_all(frame['台北'], title='column=臺北')
	#show_df_all(frame['台北']['Green'], title='column=臺北&Green')
	show_df_all(frame.loc['a'], title='key1=a')
	show_df_all(frame.loc['a']['台中'], title='key1=a, column=臺中')

	#堆疊資料
	show_df_all(frame.stack(level='縣市'))
	pprint(frame.stack(level=['縣市','顏色']))
	s1 = frame.stack(level=['縣市','顏色'])
	s1.unstack(level=['key1','顏色'])
	pprint(s1)
	s1.info()

def _main():
#	_practice_1()
	_practice_2()

if __name__ == "__main__":
	_main()
