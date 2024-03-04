WikiCost = int(input("Mbps on Wikipedia: ")) * 0.1
MemeCost = int(input("Mbps on Memes: ")) * 0.05
Total = WikiCost + MemeCost

if Total > 100:
    print("Too much consumption")
if MemeCost > WikiCost:
    print("WOW MANY MEMES\nSUCH LOL")