Hours = int(input("Hours: "))
Income = int(input("Income per hour: "))
Money = Hours * Income
PS4, Samsung, TV, Skins = 0, 0, 0, 0
Buy = True

while Buy:
    if Money < 9.99:
        Buy = False
    if Money >= 900:
        Money -= 900
        Samsung += 1
    if Money >= 500:
        Money -= 500
        TV += 1
    if Money >= 200:
        Money -= 200
        PS4 += 1
    if Money >= 9.99:
        Money -= 9.99
        Skins += 1
print(f"I can buy {PS4} PS4, {Samsung} Samsung, {TV} TV, {Skins} game skin")