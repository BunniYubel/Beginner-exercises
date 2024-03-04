Years = int(input("Years: "))
Kids = int(input("Kids: "))
MoneyPerMonth = int(input("Monthly income: "))
Total = MoneyPerMonth + 20 * Years + 30 * Kids

print(f"The total amount is {Total}$. "
      f"{MoneyPerMonth}$ minimum wage + "
      f"{20*Years}$ for {Years} years experience + "
      f"{30*Kids}$ for {Kids} kids + ")
