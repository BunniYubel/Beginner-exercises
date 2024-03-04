import random

Geometry, Algebra, Physics = (int(input("Geometry: ")),
                              int(input("Algebra: ")),
                              int(input("Physics: ")))

Average = (Geometry + Algebra + Physics) / 3
print(f"Average = {Average}")

if Average < 4:
    print("Failed, you really need to work harder!")
elif Average <= 6:
    print("You need to work harder!")
else:
    print("Good job!")