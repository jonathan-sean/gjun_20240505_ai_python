import numpy as np
import matplotlib.pyplot as plt

def practice_1():
	l:list[list] = [[1, 2, 3],
					[4, 5, 6]]
	print(f"l type: {type(l)}")
	n1 = np.array(l)
	print(n1)
	print(f"n1 type: {type(n1)}")
	print(f"n1 dimension: {n1.ndim}")
	print(f"n1 shape: {n1.shape}")
	print(f"n1 size {n1.size}")
	print(f"n1 data type: {n1.dtype}")

def main():
	practice_1()

if __name__ == "__main__":
	main()
