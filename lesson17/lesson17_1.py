import numpy as np
import pandas as pd

def _practice_1():
	# numpy 可直接建立二維的隨機陣列
	students = np.random.randint(50, 101, size=(50, 5))
	# Convert nympy ndaray to DataFrame of pandas
	stu = pd.DataFrame(students,
					  columns=['國文', '英文', '數學', '地理', '歷史'],
					  index=[f"第{n}號" for n in range(1,51)])
	print(f"Pandas DataFrame:\n{stu.to_markdown()}")
	print("\n陣列運算，使用數學運算子: {}".format(stu['國文'] + stu['英文']))
	print("\n陣列運算，使用比較運算子: {}".format(stu['國文'] >= 60))
	print("\nSerial 運算: {}".format(stu['國文'].sum()))
	print("\nnumpy 運算: {}".format(np.sum(stu['國文'])))
	print("\nDataFrame 執行統計:")
	stu['總分'] = stu.iloc[:,0:5].sum(axis=1)
	stu['平均'] = stu.iloc[:,0:5].mean(axis=1)
	print(stu)
	print("\nNumpy 執行統計:")
	stu['總分'] = np.sum(stu.iloc[:,0:5], axis=1)
	stu['平均'] = np.mean(stu.iloc[:,0:5], axis=1)
	print(stu)
	print("\nSorting:")
	print(stu['總分'].sort_values())
	print("--> 取前五名")
	sorted_s = stu['總分'].sort_values(ascending=False)
	print(sorted_s[:5])
	print("\nSorting by DataFrame:")
	sorted_df = stu.sort_values(by='總分', ascending=False)
	print("--> 取前五名")
	print(sorted_df[:5].to_markdown())
	print("\nRanking:")
	sorted_df['排名'] = sorted_df['平均'].rank(ascending=False, method='first')
	print(sorted_df.to_markdown())
	print("\n比較運算子的範例 -")
	print("--->> 國文不及格者")
	print(sorted_df[sorted_df['國文'] < 60].to_markdown())
	print("--->> 國文及英文及格者")
	print(sorted_df[(sorted_df['國文'] >= 60) & (sorted_df['英文'] >= 60)].to_markdown())
	print(sorted_df[(sorted_df['國文'] >= 60) & (sorted_df['英文'] >= 60)].count())


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
