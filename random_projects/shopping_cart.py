item = input("what item would you like to buy: ")
price = float(input("what is the price: "))
quantity = int(input("how many would you like?: "))

total = quantity * price
print(f"you have bought {quantity} x {item}s")
print(f"your total is: ${round(total, 2)}")