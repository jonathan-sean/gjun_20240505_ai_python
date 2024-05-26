# Python data structure

# tuple, it isn't standard Python data structure, just memory data temporary
# Can not change value after created

# Declare tuple variable
t1 = (1, 2, 3, "John")
print(t1)
for i in t1:
	print(i)

t2:tuple[int] = (1, 2, 3, 4)
print(t2)
for i in t2:
	print(i)

# Assign each tuple element to associated parameter
(name, height, weight) = ("Tom", 180, 78)
print(f"{name}, {height}cm, {weight}Kg")
name, height, weight = "Tom", 180, 78
print(f"{name}, {height}cm, {weight}Kg")
