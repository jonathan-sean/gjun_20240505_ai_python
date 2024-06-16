# How to draw pie chart ?
# Please visit https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html
import matplotlib.pyplot as plt

def main():
	labels:list = ['Nokia', 'Samsung', 'Apple', 'Lumia']
	values:list = [20, 30, 45, 10]
	colors:list = ['yellow', 'green', 'red', 'blue']

	# 把 Nokia 切出來
	explode = (0.3, 0, 0, 0)

	fig = plt.figure(figsize=(4.9, 4.15))
	axes = fig.add_subplot()
	axes.pie(
		values,
		center=(0.25, 0.1),
		radius=1.3,
		labels=labels,
		colors=colors,
		shadow=True,
		startangle=180.0,
		explode=explode,
		autopct='%1.1f%%')
	plt.show()

if __name__ == "__main__":
	main()
