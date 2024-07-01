# 相關係數 (correlation coefficient)
import pandas_datareader.data as pdr
import yfinance as yf
import pandas as pd
from MyPackage import *

def _add_percentage(val:float):
	#return "{:%.4f%%}".format(round(val, ndigits=4))
	return "{}%".format(round(val*100, ndigits=4))

def _practice_1():
	yf.pdr_override()
	stock_lst = ['2330.TW', '2303.TW', '2454.TW', '2317.TW']
	all_data = {ticker: pdr.get_data_yahoo(ticker) for ticker in stock_lst}
	#print(all_data)
	#print(type(all_data))
	# Convert yfinance data to pandas dataFrame
	df1 = pd.DataFrame({key:df['Adj Close'] for key,df in all_data.items()})
	summary_markdown(df1)
	#df1 = prices.dropna()
	#_summary_markdown(df1)
	df1.info()
	name_map = {'2330.TW':'臺積電', '2303.TW':'聯電', '2454.TW':'聯發科', '2317.TW':'鴻海'}
	df2 = df1.rename(columns=name_map)
	summary_markdown(df2)
	df3 = df2.dropna()
	summary_markdown(df3)
	# Get changed data
	df4 = df3.pct_change()
	summary_markdown(df4)
	# Remove invalid data
	df5 = df4.drop('2001-07-23')
	summary_markdown(df5)
	df6 = df5.map(_add_percentage)
	summary_markdown(df6)
	print("\n計算漲跌")
	df7 = df3 - df3.shift(1)
	# First record always Nan, so list from second
	summary_html(df7[1:])
	#df8 = df7.dropna()
	#_summary_markdown(df8)
	print("\n顯示相關係數")
	full_html(df5.corr())


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
