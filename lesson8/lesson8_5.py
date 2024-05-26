# dict: dictionary, key=value, not a serial data, is mapping data

d1:dict[str, int] = {"k1":1, "k2":2, "k3":3, "k4":4}
print(f"d1 {d1}")
print(str.format("d1['k1'] = {}", d1['k1']))
print(str.format("d1['k3'] = {}", d1['k3']))

d2:dict[int, str] = {1:"v1", 2:"v2", 3:"v3", 4:"v4"}
print(f"d2 {d2}")
print(str.format("d2[1] = {}", d2[1]))
print(str.format("d2[4] = {}", d2[4]))

print("Add 5=v5 to d2")
d2[5] = 'v5'
print(f"d2 {d2}")

print("Remove key 3 of d2")
del d2[3]
print(f"d2 {d2}")

print("List d1 keys with for..in loop")
for d in d1:
	print(d)
