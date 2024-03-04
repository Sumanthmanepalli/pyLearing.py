def revers_str(str):
    revr_str=""
    for s in str:
        revr_str= s+revr_str
    return revr_str

original_str=input("enter you are name")
revr_str=revers_str(original_str)
if original_str==revr_str:
    print("its a palindrome")
else:
    print("its not a palindrome")

