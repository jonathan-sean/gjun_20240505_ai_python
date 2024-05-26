# list
t1 = (1, 2, 3, 4)
print(str.format("t1 type: {}", type(t1)))

l1 = [1, 2, 3, 4]
print(str.format("l1 type: {}", type(l1)))
print(l1[0])
print(l1[1])
print(str.format("l1 {} include {} elements", l1, len(l1)))
print("list all elements with for..in loop")
for i in l1:
	print(i)

print("Append 12 to l1")
l1.append(12)
print(f"l1 {l1}")

print("Insert 4 to index 2")
l1.insert(2, 4)
print(f"l1 {l1}")

print("Remove value 4")
# This will remove first '4'
l1.remove(4)
print(f"l1 {l1}")

print("Pop last element")
n = l1.pop()
print(f"n = {n}")
print(f"l1 {l1}")

print("Pop index 1 element")
n = l1.pop(1)
print(f"n = {n}")
print(f"l1 {l1}")

print("Clear all elements")
l1.clear()
print(f"l1 {l1}")

l1 = [11, 2, 33, 44]
p
