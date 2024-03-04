Food = input("What do you want to eat? ")
print(f"{Food} {'1.50' if Food.lower() == 'hot dog' else 3 if Food.lower() == 'pizza' else 5 if Food.lower() == 'burger' else''}$")