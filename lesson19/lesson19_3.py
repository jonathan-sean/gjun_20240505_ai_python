import numpy as np
import pandas as pd
from MyPackage.myDisp import *

def _practice_1():
	s1 = pd.Series(
		np.random.randn(9),
		index=[
			['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
			['1', '2', '3', '1', '2', '3', '1', '2', '3'],
		],
	)
	pprint(s1)

def _main():
	_practice_1()

if __name__ == "__main__":
	_main()
