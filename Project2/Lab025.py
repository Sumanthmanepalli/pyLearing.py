side1 = int(input("enter the side 1 value"))
side2 = int(input("enter the side 2 value"))
side3 = int(input("enter the side 3 value"))

if side1==side2==side3:
    print("all are equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("ISO two sides are equal")

else:
    print("all are scalene")