Duration = int(input("Call duration (in seconds): "))
Cost = 25 + (Duration * (0.01 if Duration < 501 else 0.008 if Duration < 801 else 0.005))
print(f"Total amount: {Cost}")