Price = int(input("Price: "))
Tax = int(input("Tax: "))/100 + 1
Total = Price * Tax

print(f"The total price of the laptop is {Total}$")