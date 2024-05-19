try:
	money = int(input("請輸入金額: "))
	print(f"Your input is {money}")
except ValueError:
	print("Invalid value, check your input.")
except Exception:
	print("Something wrong, check your input.")
print("End this example.")
