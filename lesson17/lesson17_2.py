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
	print("\n使用 query() 搜尋值 -")
	print("--->> 國文不及格者")
	print(stu.query('國文<60').to_markdown())
	print("--->> 國文及英文及格者")
	print(stu.query('國文>=60 and 英文>=60').to_markdown())


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
