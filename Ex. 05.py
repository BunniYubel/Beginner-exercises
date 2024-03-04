Money = int(input("Money: "))
Bitcoin = int(input("Bitcoin price: "))
Ethereum = int(input("Ethereum price: "))
Litecoin = int(input("Litecoin price: "))

print(f"With ${Money} you can buy: {Money//Bitcoin} Bitcoin(s), "
      f"{Money//Ethereum} Ethereum, "
      f"and {Money//Litecoin} Litecoin(s)")