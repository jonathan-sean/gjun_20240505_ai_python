# 陣列運算
# 可做陣列運算的資料結構 package
#  1. numpy
#  2. scipy
#  3. Pandas
import numpy as np
import matplotlib.pyplot as plt

def practice_1():
	n1 = np.array([1, 3, 5, 7, 9])
	print(type(n1))
	n2 = np.array([2, 4, 6, 8, 10])
	print(type(n2))
	# 陣列運算
	n3 = n1 + n2
	print(f"n1 + n2 = {n3}")
	n4 = n3 * 10 / 5 ** 2
	# Convert numpy ndarray to python list
	lst = n4.tolist()
	print(lst)

def practice_2():
	x = np.linspace(-3, 3, num=50)
	y = 2 * x +1
	z = x ** 2
	#print(f"x: {x}\ny: {y}\nz: {z}")
	fig = plt.figure()
	axes = fig.add_subplot()
	axes.plot(x, y, color="red", linewidth=1.0, linestyle="--")
	axes.plot(x, z, color="blue", linewidth=1.0, linestyle="-.")
	plt.show()

def practice_3():
	t = np.arange(0, 2.5, 0.1)
	#print(t)
	y1 = np.sin(t * np.pi)
	y2 = np.cos(t * np.pi)
	fig = plt.figure()
	axes = fig.add_subplot()
	axes.plot(t, y1, 'b*')
	axes.plot(t, y2, 'r^')
	plt.show()

def practice_4():
	t = np.arange(0, 2.5, 0.1)
	#print(t)
	y1 = np.sin(t * np.pi)
	y2 = np.cos(t * np.pi)
	fig = plt.figure()
	axes1 = fig.add_subplot(2, 1, 1)
	axes2 = fig.add_subplot(212)
	axes1.plot(t, y1, 'b-.')
	axes2.plot(t, y2, 'r-.')
	plt.show()


def main():
#	practice_1()
#	practice_2()
#	practice_3()
	practice_4()

if __name__ == "__main__":
	main()
