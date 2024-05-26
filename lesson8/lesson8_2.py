def menu(wine:str, entree:str, dessert:str)->None:
	print(f"酒類: {wine}");
	print(f"主餐: {entree}");
	print(f"甜點: {dessert}");

# Parameter with default argument
def menu_2(wine:str, entree:str="羊排", dessert:str="奶昔")->None:
	print(f"酒類: {wine}");
	print(f"主餐: {entree}");
	print(f"甜點: {dessert}");

# If parameter lead with '*' that must call by arguments only
# and the argument quantity is unlimited
# The argument can be ignored
def print_args(*args:any):
	print(f"args is tuple: {args}")

# If parameter lead with '**' that must call by argument with parameter name
# and the argument quantity is unlimited
# The argument can be ignored
def print_kwargs(**kwargs):
	print(f"kwargs is dict: {kwargs}")

# combo
def print_args_kwargs(*args, **kwargs):
	print(f"args is tuple: {args}")
	print(f"kwargs is dict: {kwargs}")

# This function cannot work
# '*args' need before '**kwargs'
#def print_kwargs_args(**kwargs, *args):
#	print(f"args is tuple: {args}")
#	print(f"kwargs is dict: {kwargs}")

# Call by arguments
# Arguments must follow the order of parameters
menu("白酒", "牛排", "蛋糕")
print("------------------")
menu("紅酒", "雞排", "冰淇淋")

print("\n====================\n")
# Assign argument to specific parameter name
menu(wine="白酒", dessert="蛋糕", entree="牛排")
print("------------------")
menu(entree="雞排", wine="紅酒", dessert="冰淇淋")

print("\n====================\n")
# Mixed mode
menu("白酒", dessert="蛋糕", entree="牛排")
print("------------------")
menu("白酒", entree="牛排", dessert="蛋糕")
print("------------------")
# Below will be failure
# Must set parameter for all arguments if first argument with parameter name
#menu(entree="雞排", wine="紅酒", "冰淇淋")
menu(entree="雞排", wine="紅酒", dessert="冰淇淋")

print("\n====================\n")
menu_2("白酒", "牛排")
print("------------------")
menu_2(entree="牛排", wine="白酒")
print("------------------")
menu_2("紅酒", "雞排", "冰淇淋")
print("------------------")
# If use parameter name, '冰淇淋' will assign to entree
#menu_2("紅酒", "冰淇淋")
menu_2("紅酒", dessert="冰淇淋")

print("\n====================\n")
print_args()
print_args(1, 2, 4.5, 'c', "test")
# Cannot use the parameter name
#print_args(1, 2, 4.5, 'c', key="test")

print("\n====================\n")
print_kwargs()
# Need use parameter name for each argument
#print_kwargs(1, key2=2, key3=4.5, key4='c', key5="test")
print_kwargs(key1=1, key2=2, key3=4.5, key4='c', key5="test")

print("\n====================\n")
print_args_kwargs()
print("------------------")
print_args_kwargs(1, 2, 4.5, 'c', "test", key1=1, key2=2, key3=4.5, key4='c', key5="test")
# Below will failure
#print_args_kwargs(1, 2, 4.5, 'c', key1=1, "test", key2=2, key3=4.5, key4='c', key5="test")
print("------------------")
print_args_kwargs(key1=1, key2=2, key3=4.5, key4='c', key5="test")
print("------------------")
print_args_kwargs(1, 2, 4.5, 'c', "test")

#print("\n====================\n")
#print_kwargs_args()
#print("------------------")
#print_kwargs_args(key1=1, key2=2, key3=4.5, key4='c', key5="test", 1, 2, 4.5, 'c', "test")


print("\n====================\n")
print()
print(1, 2, 3, 4, end=' ', sep=',')
print(5, 6, 7, 8)
print(9, 0)
