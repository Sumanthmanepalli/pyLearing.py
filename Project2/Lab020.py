
num1 = int(input("enter the no 1"))
num2 = int(input("enter the no 2"))
num3 = int(input("enter the no 3"))

#max_num = max(num1, num2, num3)
#print(max_num)

if num1>num2 and num1>num3 :
    print("max is ",num1)
elif num2>num1 and num2>num3:
    print("max is ", num2)
else:
    print("max is", num3)