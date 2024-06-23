import numpy as np
import matplotlib.pyplot as plt

def practice_1():
	# numpy 可直接建立二維的隨機陣列
	students = np.random.randint(50, 101, size=(50, 5))
	print(students)
	# 選取二維陣列中的 element 可用 array[row(axis 0),column(axis 1)] 方式
	print(f"第一位學生的第一科分數: {students[0,0]}")	# first score of first student
	print(f"最前一位學生的分數: {students[:1]}")		# first 1 student
	print(f"最前二位學生的分數: {students[:2]}")		# first 2 students
	print(f"最後五位學生的分數: {students[-5:]}")	# last 5 students
	print(f"從第六位學生開始的學生分數: {students[5:]}")		# from first 6 student to last
	print(f"所有學生的第一科分數: {students[:0,1]}")
	print(f"所有學生的最後一科分數: {students[:0,-1]}")
	print(f"第一位學生的總分: {np.sum(students[:1])}")
	print(f"最前二位學生的總分: {np.sum(students[:2],axis=1)}")
	print(f"全班每位學生的總分: {np.sum(students,axis=1)}")
	print(f"每一科全班的平均: {np.mean(students,axis=0)}")
	print(f"每一科全班的中位數: {np.median(students,axis=0)}")


def main():
	practice_1()

if __name__ == "__main__":
	main()
