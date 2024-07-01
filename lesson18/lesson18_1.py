# 相關係數 (correlation coefficient)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def _display_dataframe(df):
	print(df.iloc[:5,:].to_markdown())
	print("....    ....")
	print(df.iloc[-5:,:].to_markdown())

def _practice_1():
	data = {'年廣告費投入':[12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9],
			'月均銷售額':[21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]}
	df1 = pd.DataFrame(data, index=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
	_display_dataframe(df1)
	print("The correlation coefficient is {}".format(df1['年廣告費投入'].corr(df1['月均銷售額'])))
	figure = plt.figure(figsize=(8,5))
	axes = figure.add_subplot(1,1,1)
	axes.plot(df1.index,df1['年廣告費投入'].values,'ro--')
	axes.plot(df1.index,df1['月均銷售額'].values,'bo--')
	plt.show()

def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
