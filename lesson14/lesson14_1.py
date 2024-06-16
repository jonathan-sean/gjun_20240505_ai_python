import matplotlib.pyplot as plt

def practice_1():
	# 1.製作figure
	fig = plt.figure()

	# 2.在1.的figure上製作一個axes
	ax_1 = fig.add_subplot(1, 1, 1)

	# 3.將圖的數據儲存在axes中
	X = [0, -1, 2]
	Y = [3, 6, -5]
	ax_1.plot(X, Y, 'bo')

	# 4.顯示圖
	plt.show()

def practice_2():
	fig = plt.figure()
	axes1 = fig.add_subplot(1, 3, 1)
	axes1.set_title("title1")
	axes2 = fig.add_subplot(1, 3, 2)
	axes2.set_title("title2")
	axes3 = fig.add_subplot(1, 3, 3)
	axes3.set_title("title3")
	plt.show()

def practice_3():
	index = ['apple', 'banana', 'orange', 'tomato', 'guava']
	values = [5, 7, 3, 4, 6]
	fig = plt.figure()
	axes = fig.add_subplot(1, 1, 1)
	axes.bar(index, values)

	print(str.format("xaxis: {}", axes.get_xticks()))
	print(axes.get_xticklabels())
	plt.show()


def main():
#	practice_1()
#	practice_2()
	practice_3()


if __name__ == "__main__":
	main()
