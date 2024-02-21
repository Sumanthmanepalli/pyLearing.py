a = int(input("enter factorial no\n"))
if a < 0:
    print("fact")
elif a == 0:
    print("fact-", 1)
else:
    fact = 1
    for a in range(1, a + 1):
        fact = fact * a
print("Fact ->>", fact)
