import pyinputplus as pyip

#for i in range(0, 5):
#	print(i, end=' ')
#	total += i
#print()

#for i in range(1, 10):
#	print(i, end=' ')
#	total += i
#print()

#for i in range(1, 10, 2):
#	print(i, end=' ')
#	total += i
#print()

for i in range(1, 10):
	print(f"i={i}")
	for j in range(1, 10):
		print(f"j={j}", end=' ')
	print("\n-----------------------")

try:
	n = pyip.inputInt("加總 1 到 n，請輸入 n: ", min=0, timeout=3)
	total = 0
	for i in range(n+1):
		total += i
	print(f"加總 1 到 {n} 的結果是 {total}");
except Exception as e:
	print(f"EXCEPTION - {type(e)}")
