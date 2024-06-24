import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

def practice_1():
	#print(np.arange(9).reshape((3,3)))
	df1 = pd.DataFrame(np.arange(9).reshape((3,3)),
					   index=['a', 'b', 'c'],
					   columns=['臺北', '臺中', '高雄'])
	print(df1)
	print(df1.reindex(index=['a', 'c'], columns=['臺北', '高雄']))

def practice_2():
	df2 = pd.DataFrame(np.arange(16).reshape((4,4)),
					   index=['臺北', '臺中', '臺南', '高雄'],
					   columns=['one', 'two', 'three', 'four'])
	print(df2)
	print(df2.drop(index=['臺中', '臺南']))
	print(df2.drop(index=['臺中', '臺南'], columns=['one', 'two']))

def main():
#	practice_1()
	practice_2()

if __name__ == "__main__":
	main()
