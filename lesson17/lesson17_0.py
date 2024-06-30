import pandas as pd

def format_number(value:int) -> str:
	return "{0:,}".format(value)

def _practice_1():
	df1 = pd.read_csv('上市公司資料.csv')
	df2 = df1[['公司代號', '公司名稱', '產業別', '營業收入-當月營收', '營業收入-上月營收']]
	df2.loc[:,'營業收入-當月營收'] = df2['營業收入-當月營收'].map(format_number)
	df2.loc[:,'營業收入-上月營收'] = df2['營業收入-上月營收'].map(format_number)
	print(df2)

def _practice_2():
	# Reverse the string
	value = str(7864622)[::-1]
	value2 = value[0]
	for i in range(1, len(value)):
		if i % 3 == 0:
			value2 += ','
		value2 += value[i]
	print(value2[::-1])

def format_number_2(vin:int):
	# Reverse the string
	value = str(vin)[::-1]
	value2 = value[0]
	for i in range(1, len(value)):
		if i % 3 == 0:
			value2 += ','
		value2 += value[i]
	return value2[::-1]

def _practice_3():
	df1 = pd.read_csv('上市公司資料.csv')
	df2 = df1[['公司代號', '公司名稱', '產業別', '營業收入-當月營收', '營業收入-上月營收']]
	df2.loc[:,'營業收入-當月營收'] = df2['營業收入-當月營收'].map(format_number_2)
	df2.loc[:,'營業收入-上月營收'] = df2['營業收入-上月營收'].map(format_number_2)
	print(df2)


def _main():
#	_practice_1()
#	_practice_2()
	_practice_3()

if __name__ == "__main__":
	_main()
