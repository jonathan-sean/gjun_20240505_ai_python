# 相關係數 (correlation coefficient)
import pandas_datareader.data as pdr
import yfinance as yf
import pandas as pd

def _display_dataframe(df):
	print(df.iloc[:5,:].to_markdown())
	print("....    ....")
	print(df.iloc[-5:,:].to_markdown())

def _practice_1():
	yf.pdr_override()
	df = pdr.get_data_yahoo('AAPL')
	_display_dataframe(df)

def _practice_2():
	yf.pdr_override()
	stock_lst = ['AAPL', 'IBM', 'MSFT', 'GOOG']
	#for s in stock_lst:
	#	_display_dataframe(pdr.get_data_yahoo(s))
	all_data = {ticker: pdr.get_data_yahoo(ticker) for ticker in stock_lst}
	print(all_data)
	print(type(all_data))
	# Convert yfinance data to pandas dataFrame
	prices = pd.DataFrame({key:df['Adj Close'] for key,df in all_data.items()})
	#_display_dataframe(prices)
	df1 = prices.dropna()
	_display_dataframe(df1)
	df1.info()
	_display_dataframe(df1.loc['2024'])
	_display_dataframe(df1.loc['2024-05'])
	_display_dataframe(df1.loc['2024-05-01'])

def _main():
#	_practice_1()
	_practice_2()

if __name__ == "__main__":
	_main()
