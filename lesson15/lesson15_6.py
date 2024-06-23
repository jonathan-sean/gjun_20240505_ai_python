import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

def practice_1():
	# numpy 可直接建立二維的隨機陣列
	students = np.random.randint(50, 101, size=(50, 5))
	# Convert nympy ndaray to DataFrame of pandas
	df = pd.DataFrame(students,
					  columns=['國文', '英文', '數學', '地理', '歷史'],
					  index=[f"學生#{n}" for n in range(1,51)])
	# DataFrame's subscript
	# serial data
	chinese_series = df['國文']
	print(f"國文成績:\n{chinese_series}")
	print(f"學生#49的國文成績:{chinese_series['學生#49']}")
	print(f"學生#49,50的國文成績:\n{chinese_series[['學生#49','學生#50']]}")
	print(f"最前五位學生的國文成績:\n{chinese_series[:5]}")
	print('----------------')
	#第1號的學生
	# loc 只接受 index name, not index number
	print(f"學生#1的成績:\n{df.loc['學生#1']}")
	#第1號和第2號的學生
	# 注意：loc[] 二筆以上的輸出格式為 DataFrame，和僅一筆時不同
	print(f"學生#1,5的成績:\n{df.loc[['學生#1','學生#5']]}")
	#print(f"學生#1,5的成績:\n{df.loc[[0, 4]]}")
	#前5個學生
	# iloc 只接受 index number
	print(f"最前五位學生的成績:\n{df.iloc[:5]}")
	#後5個學生
	print(f"最後五位學生的成績:\n{df.iloc[-5:]}")


def main():
	practice_1()

if __name__ == "__main__":
	main()
