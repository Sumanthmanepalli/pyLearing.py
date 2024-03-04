b = int(input("enter factorial num\n"))
if b < 0:
    print("fact")
elif b == 0:
    print("fact -", 1)
else:
    fact = 1
    for b in range(1, b + 1):
        fact = fact * b
print(fact)
