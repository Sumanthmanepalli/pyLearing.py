def revers_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str

original_str=input("enter name")
rev_str= revers_string(original_str)
print(rev_str)
if original_str==rev_str:
    print("its a palindrome")
else:
    print("not a palindrome")
