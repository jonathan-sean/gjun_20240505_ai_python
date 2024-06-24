import requests
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from IPython.display import display

def practice_1():
	url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=D162B6E0-77BB-4E1F-99A6-E3F44A0503BF'
	try:
		resp = requests.get(url)
		resp.raise_for_status()
	except Exception as e:
		print(e)
	else:
		print(resp.text)
		print(requests.utils.default_headers())

def to_int(v):
	try:
		return int(v)
	except:
		return 0

def practice_2():
	df1 = pd.read_csv("opendata112N010.csv")
	col_map = {'statistic_yyy':'統計年',
			   'site_id':'區域別',
			   'people_total':'年底人口數',
			   'area':'土地面積',
			   'population_density':'人口密度'}
#	print(df1)
	# Rename column labels
	df2 = df1.rename(columns=col_map)
#	print(df2)
	# Drop unused row
	df3 = df2.drop(index=0)
	#print(df3)
	# Drop Nan data
	df4 = df3.dropna()
	#print(df4)
	#print(df4.iloc[-10:,:])
	# Drop unused column
	df5 = df4.drop(columns=['統計年'])
	#print(df5)
	# Change index to ‘區域別’
	df6 = df5.set_index('區域別')
#	print(df6)
#	df6.info()
	# Convert data type
	df6['土地面積'] =  df6['土地面積'].astype(float)
#	print(df6)
#	df6.info()
	# Ugly process, no index, just one field data
#	nums = []
#	for n in df6['年底人口數']:
#		try:
#			nums.append(int(n))
#		except Exception as e:
#			nums.append(0)
	df6['年底人口數'] = df6['年底人口數'].map(to_int)
	#df6['年底人口數'] = df6['年底人口數'].map(lambda i: try: int(i) except: 0)
	df6['人口密度'] = df6['人口密度'].map(to_int)
	display(df6, raw=True)
	df6.info()
	df6.to_csv('人口密度.csv')
	df6.to_excel('人口密度.xlsx', sheet_name='112 年度')
	df6.to_json('人口密度.json', force_ascii=False, orient='table')
	df6.to_html('人口密度.html')
	df6.to_markdown('人口密度.md')

def practice_3():
	# Create a dataframe
	df = pd.DataFrame({
		'Product_id': ['ABC', 'DEF', 'GHI', 'JKL',
					   'MNO', 'PQR', 'STU', 'VWX'],
		'Stall_no': [37, 38, 9, 50, 7, 23, 33, 4],
		'Grade': [1, 0, 0, 2, 0, 1, 3, 0],
		'Category': ['Fashion', 'Education', 'Technology',
					 'Fashion', 'Education', 'Technology',
					 'Fashion', 'Education'],
		'Demand': [10, 12, 14, 15, 13, 20, 10, 15],
		'charges1': [376, 397, 250, 144, 211, 633, 263, 104],
		'charges2': [11, 12, 9, 13, 4, 6, 13, 15],
		'Max_Price': [4713, 10352, 7309, 20814, 9261,
					  6104, 5257, 5921],
		'Selling_price': [4185.9477, 9271.490256, 6785.701362,
						  13028.91782, 906.553935, 5631.247872,
						  3874.264992, 4820.943]
	})
	print(df)

def main():
#	practice_1()
	practice_2()
#	practice_3()

if __name__ == "__main__":
	main()
