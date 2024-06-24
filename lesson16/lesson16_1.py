import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

def practice_1():
	# numpy 可直接建立二維的隨機陣列
	students = np.random.randint(50, 101, size=(50, 5))
	# Convert nympy ndaray to DataFrame of pandas
	stu = pd.DataFrame(students,
					  columns=['國文', '英文', '數學', '地理', '歷史'],
					  index=[f"第{n}號" for n in range(1,51)])
	# DataFrame's subscript
	# serial data
	print(f"Indies:\n{stu.index}, {len(stu.index)}")
	print(f"Columns:\n{stu.columns}, {len(stu.columns)}")
	print("使用陣列運算取出所有學生的總分")
	sum_series = stu['國文'] + stu['英文'] + stu['數學'] + stu['地理'] + stu['歷史']
	#print(f"total:\n{sum_series}")
	average_series = sum_series / len(stu.columns)
	stu['總分'] = sum_series
	stu['平均'] = average_series
	print(stu)
	print(f"Columns:\n{stu.columns}, {len(stu.columns)}")
	print(stu.iloc[:,:5])
	print(stu[['國文', '英文', '數學', '歷史']])
	print("學生成績總分計算")
	print("用 numpy.sum()")
	print(np.sum(stu.iloc[:,:5], axis=1))
	print("用 DataFrame.sum()")
	print(stu.iloc[:,:5].sum(axis=1))


def main():
	practice_1()

if __name__ == "__main__":
	main()
