from math import pi

radius = float(input("enter the radius"))
area = float(pi * radius * 2)
print(area)

a = input("enter the first number")
b = input("enter the second number")
if a == b:
    print("the first number is equal to second number")
elif a > b:
    print("the first number is greater than the second number")
elif a < b:
    print("the second number is greater than to first number")

num = int(input("Enter any number is"))
'''sqrt=num**2
print("The Square root of the under given number is:- ",sqrt)
cube=sqrt**3
print("the square and cube of a given number is ", cube)'''
cube = (num ** 2) ** 3
print("the square and cube of a given number is ", cube)
