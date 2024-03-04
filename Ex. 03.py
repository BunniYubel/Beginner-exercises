bitcoin = int(input("Bitcoin: "))
increase = int(input("percentage as an integer: "))/100
total = bitcoin * (1 + increase)
difference = total - bitcoin

print(f"Total: {total}")
print(f"Difference: {difference}")