import matplotlib.pyplot as plt
from pprint import pprint

def practice_1():
	idx = [3, 4, 5, 6, 7]
	vals = [5000, 6000, 7000, 8000, 9000]
	fig = plt.figure()
	axes = fig.add_subplot(1, 1, 1)
	axes.bar(idx, vals)
	print(str.format("xaxis: {}", axes.get_xticks()))
	pprint(axes.get_xticklabels())
	plt.show()

def practice_2():
	idx = [3, 4, 5, 6, 7]
	vals = [5000, 6000, 7000, 8000, 9000]
	fig = plt.figure()
	axes = fig.add_subplot(1, 1, 1)
	axes.bar(idx, vals)
	subj = ['apple', 'banana', 'orange', 'tomato', 'guava']
	axes.set_xticks(idx, subj)
	# 圖形四個角落的座標值
	print(axes.axis())
	xmin, xmax, ymin, ymax = axes.axis()
	xmin -= 0.2
	xmax += 0.2
	ymin = 3000
	ymax += 1000
	# 指定圖形四個角落的座標值
	#axes.axis(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
	axes.axis([xmin, xmax, ymin, ymax])
	print(axes.axis())
	print(str.format("xaxis: {}", axes.get_xticks()))
	pprint(axes.get_xticklabels())
	plt.show()

def practice_3():
	idx = [3, 4, 5, 6, 7]
	vals = [5000, 6000, 7000, 8000, 9000]
	# 用 index 取值
	for i,v in enumerate(idx):
		print(i, v, vals[i])
	# 用 zip() 製作 tuple
	for t in zip(idx, vals):
		print(t)
	# 再把 tuple 直接印出
	for x,y in zip(idx, vals):
		print(x, y)

def practice_4():
	idx = [3, 4, 5, 6, 7]
	vals = [5000, 6000, 7000, 8000, 9000]
	fig = plt.figure()
	axes = fig.add_subplot(1, 1, 1)
	axes.bar(idx, vals)
	subj = ['apple', 'banana', 'orange', 'tomato', 'guava']
	axes.set_xticks(idx, subj)

#	for x,y in zip(idx, vals):
#		axes.annotate(str(y), (x, y))
	# 上面的設定會偏，fine tune the position
	for x,y in zip(idx, vals):
		axes.annotate(str(y), (x-0.15, y+100))
	# 圖形四個角落的座標值
	print(axes.axis())
	xmin, xmax, ymin, ymax = axes.axis()
	xmin -= 0.2
	xmax += 0.2
	ymin = 3000
	ymax += 1000
	# 指定圖形四個角落的座標值
	#axes.axis(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
	axes.axis([xmin, xmax, ymin, ymax])
	print(axes.axis())
	print(str.format("xaxis: {}", axes.get_xticks()))
	pprint(axes.get_xticklabels())
	plt.show()

def practice_5():
	idx = [3, 4, 5, 6, 7]
	vals = [5125, 3456, 7788, 4785, 9999]
	fig = plt.figure()
	axes = fig.add_subplot(1, 1, 1)
	# be careful the type format => fmt = '[marker][line][color]'
	# marker, line, color 只能指定一次
	axes.plot(idx, vals, 'go-.')
	subj = ['apple', 'banana', 'orange', 'tomato', 'guava']
	axes.set_xticks(idx, subj)

#	for x,y in zip(idx, vals):
#		axes.annotate(str(y), (x, y))
	# 上面的設定會偏，fine tune the position
	for x,y in zip(idx, vals):
		axes.annotate(str(y), (x-0.15, y+200))
	# 圖形四個角落的座標值
	print(axes.axis())
	xmin, xmax, ymin, ymax = axes.axis()
	xmin -= 0.2
	xmax += 0.2
	ymin = 3000
	ymax += 1000
	# 指定圖形四個角落的座標值
	#axes.axis(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
	axes.axis([xmin, xmax, ymin, ymax])
	print(axes.axis())
	print(str.format("xaxis: {}", axes.get_xticks()))
	pprint(axes.get_xticklabels())
	plt.show()

def practice_6():
	student1 = {'chinese':78, 'english':80, 'math':92, 'history':75, 'discover':85}
	student2 = {'chinese':92, 'english':60, 'math':85, 'history':88, 'discover':90}
	subjs = list(student1.keys())
	val1 = list(student1.values())
	val2 = list(student2.values())
	fig = plt.figure(figsize=(8,5))
	axes = fig.add_subplot(1, 1, 1)
	axes.plot(subjs, val1, 'bo--')
	axes.plot(subjs, val2, 'r.-')
	plt.show()


def main():
#	practice_1()
#	practice_2()
#	practice_3()
#	practice_4()
#	practice_5()
	practice_6()


if __name__ == "__main__":
	main()
