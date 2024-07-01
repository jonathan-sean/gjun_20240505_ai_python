import pandas as pd
from datetime import datetime

def _practice_1():
	all_data = pd.read_csv('world.csv')
	all_data.info()
	print("\nReindex with '洲名','國家','日期','總確診數','新增確診數'")
	df1 = all_data.reindex(columns=['洲名','國家','日期','總確診數','新增確診數'])
	df1['日期'] = pd.to_datetime(df1['日期'])
	df1.info()
	print(df1.iloc[:5,:].to_markdown())
	print("\nQuery Taiwan -")
	tw_df = df1.query('國家=="台灣"')
	print(tw_df.iloc[:5,:].to_markdown())
	print("\nQuery Japan -")
	jp_df = df1.query('國家=="日本"')
	print(jp_df.iloc[:5,:].to_markdown())
	print("\nSearch Taiwan with year and month (Use subscript) -")
	print(tw_df[(tw_df['日期'].dt.year == 2022) & (tw_df['日期'].dt.month == 6)].iloc[:5,:].to_markdown())
	print(tw_df[(tw_df['日期'].dt.year == 2022) & (tw_df['日期'].dt.month < 6)].iloc[:5,:].to_markdown())
	print(tw_df[(tw_df['日期'].dt.year == 2022) & (tw_df['日期'].dt.month < 6)].iloc[-5:,:].to_markdown())
	print("\nSearch Japan with year and month (Use subscript) -")
	print(jp_df[(jp_df['日期'].dt.year == 2022) & (jp_df['日期'].dt.month == 6)].iloc[:5,:].to_markdown())
	print(jp_df[(jp_df['日期'].dt.year == 2022) & (jp_df['日期'].dt.month < 6)].iloc[:5,:].to_markdown())
	print(jp_df[(jp_df['日期'].dt.year == 2022) & (jp_df['日期'].dt.month < 6)].iloc[-5:,:].to_markdown())
	print("\nSearch Taiwan with year and month (Use query) -")
	print(tw_df.query('日期>="2022-01-01" and 日期<="2022-06-30"').iloc[:5,:].to_markdown())
	print("\nSearch Taiwan 新增確診數 (Use query) -")
	print(tw_df.query('新增確診數>=10000').iloc[:5,:].to_markdown())
	print("\nSearch Taiwan by user input year (Use query) -")
	year = int(input("Input year: "))
	print(tw_df[(tw_df['日期'].dt.year == year)].iloc[:5,:].to_markdown())
	# Below line will fail
	#year = int(input("Input year: "))
	#search_str1 = f"{year}-01-01"
	#search_str2 = f"{year}-12-31"
	#print(f"{search_str1}, {search_str2}")
	#print(tw_df(tw_df.query('日期>=@search_str1 and 日期<=@search_str2').iloc[:5,:].to_markdown()))
	#search_str = f'日期>="{year}-01-01" and 日期<="{year}-12-31"'
	#print(search_str)
	#print(tw_df(tw_df.query('@search_str').iloc[:5,:].to_markdown()))
	n = int(input("Input 新增確診數: "))
	print(tw_df.query('新增確診數>=@n').iloc[:5,:].to_markdown())



def _practice_2():
	one_day = datetime.fromisoformat('2024-06-30')
	print(one_day.year)
	print(one_day.month)
	print(one_day.day)

def _main():
	_practice_1()
#	_practice_2()

if __name__ == "__main__":
	_main()
