Years = int(input("Years: "))
Kids = int(input("Kids: "))
MoneyPerMonth = int(input("Monthly income: "))
DaysMissed = int(input("Days Missed: "))
Total = MoneyPerMonth + 20 * Years + 30 * Kids
if DaysMissed == 0:
    Total += 100
print(f"The total amount is {Total}. "
      f"{MoneyPerMonth}$ minimum wage + "
      f"{20*Years}$ for {Years} years experience + "
      f"{30*Kids}$ for {Kids} kids + "
      f"{100 if DaysMissed == 0 else 0}$ for{' not' if DaysMissed == 0 else ''} missing a day at work")
