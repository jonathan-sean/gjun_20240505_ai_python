import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def practice_1():
	# numpy 可直接建立二維的隨機陣列
	students = np.random.randint(50, 101, size=(50, 5))
	# Convert nympy ndaray to DataFrame of pandas
	df = pd.DataFrame(students,
					  columns=['國文', '英文', '數學', '地理', '歷史'],
					  index=[f"學生#{n}" for n in range(1,51)])
	print(f"Pandas DataFrame:\n{df}")
	#print(df.values)	# Recommend to use to_numpy() instead
	print(f"Convert DataFrame to numpy:\n{df.to_numpy()}")
	print(f"Convert DataFrame to python list:\n{df.to_numpy().tolist()}")


def main():
	practice_1()

if __name__ == "__main__":
	main()
