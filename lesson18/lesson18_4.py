import numpy as np
import pandas as pd
from MyPackage import *

def summary_markdown(df, first=5, last=5):
#	if type(df) != 'pandas.core.frame.DataFrame':
#		print(df)
#		return
	if first > 0:
		print(df.iloc[:first,:].to_markdown())
		print("....    ....")
	print(df.iloc[-last:,:].to_markdown())

def full_markdown(df):
	summary_markdown(df, first=0, last=0)

def _show_html(df):
	tmpf = tempfile.NamedTemporaryFile(suffix='.html').name
	df.to_html(tmpf)
	os.system("w3m -dump {}".format(tmpf))

# Return value
def _abc(s):
	return s.mean()

# Return new series data
# Can return multiple data
def _efg(s):
	return pd.Series([s.mean(), s.max(), s.min()],
	                 index=['平均', '最高分', '最低分'])

# Return new series data
# Can return multiple data
def _efg_2(s):
	max_name = s[s == s.max()].index.values.tolist()[0]
	min_name = s[s == s.min()].index.values.tolist()[0]
	return pd.Series([s.mean(), f"{max_name}:{s.max()}", f"{min_name}:{s.min()}"],
	                 index=['平均', '最高分', '最低分'])

# Return new series data
# Can return multiple data
def _efg_3(s):
	print("s[s == s.max()]: \n{}".format(s[s == s.max()]))
	max_name = s[s == s.max()].index.values.tolist()[0]
	min_name = s[s == s.min()].index.values.tolist()[0]
	less60 = ",".join(list(s[s < 60].index))
	return pd.Series([s.mean(), f"{max_name}:{s.max()}", f"{min_name}:{s.min()}", less60],
	                 index=['平均', '最高分', '最低分', '不及格科目'])

def _practice_1():
	# numpy 可直接建立二維的隨機陣列
	students = np.random.randint(50, 101, size=(50, 5))
	# Convert nympy ndaray to DataFrame of pandas
	stu = pd.DataFrame(students,
					  columns=['國文', '英文', '數學', '地理', '歷史'],
					  index=[f"第{n}號" for n in range(1,51)])
	summary_markdown(stu)
#	print(stu.apply(_abc))
#	print(stu.apply(_abc, axis=1))
	#summary_markdown(stu.apply(_abc, axis=1))
#	summary_markdown(stu.apply(_efg, axis=1))
	print("\n學生成績統計資料 - 1")
	full_markdown(stu.apply(_efg, axis=1))
	#print("\nScore of first student")
	#stu1 = stu.iloc[0]
	#print(stu1)
	#print(stu1[stu1 == stu1.max()].index.values.tolist()[0])
	print("\n學生成績統計資料 - 2")
	full_markdown(stu.apply(_efg_2, axis=1))
	print("\n學生成績統計資料 - 3")
	expend_stu = stu.apply(_efg_3, axis=1)
	full_markdown(expend_stu)
	print("\n整合後的學生成績統計資料")
	combined_data = pd.concat([stu, expend_stu], axis=1)
	full_html(combined_data)


def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
