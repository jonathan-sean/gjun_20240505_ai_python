import pyinputplus as pyip

try:
	n = pyip.inputInt(f"請輸入整數，求所有的公因數: ", min=0)
	print(f"{n} 的因數有 ", end='')
	for i in range(1, n+1):
		if n % i == 0:
			if i >= n:
				print(i)
			else:
				print(i, end=', ')
	#print()
except Exception as e:
	print(f"EXCEPTION - {type(e)}")
