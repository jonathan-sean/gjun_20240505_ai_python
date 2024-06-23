def practice_1():
	n1 = [1, 3, 5, 7, 9]
	n2 = [2, 4, 6, 8, 10]
	add_list = []
	for f,s in zip(n1,n2):
		add_list.append(f+s)
	print(add_list)

def practice_2():
	n1 = [1, 3, 5, 7, 9]
	n2 = [2, 4, 6, 8, 10]
	# list comprehension(快速建立)
	add_list = [f+s for f,s in zip(n1,n2)]
	print(add_list)


def main():
	practice_1()
	practice_2()

if __name__ == "__main__":
	main()
