Product = int(input("Price of product: "))
Place = input("Are you from the US, Europe, Canada, or other? ").lower()

print(f"You have to pay {Product + (5 if Place == 'us' else 7 if Place == 'europe' else 3 if Place == 'canada' else 9 if Place =='other' else '')}$, "
      f"{Product}$ for the product and "
      f"{5 if Place == 'us' else 7 if Place == 'europe' else 3 if Place == 'canada' else 9}$ for shipping cost")