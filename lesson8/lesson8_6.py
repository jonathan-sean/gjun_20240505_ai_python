# set

# set will auto remove duplicated elements and sorted
set1:[int] = {1, 1, 2, 2, 3, 3, 5, 4}
#set1 = {1, 1, 2, 2, 3, 3, 5, 4}
print(str.format("set1 type: {}", type(set1)))
print(f"set1: {set1}")

set2 = {"ab", "cd", "ef", "gh", "gh"}
print(f"set2: {set2}")

print("Convert set set1 to list l1");
#l1:[int] = list(set1)
l1 = list(set1)
print(f"l1: {l1}")
