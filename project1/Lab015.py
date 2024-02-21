s = ''.join(e for e in s if e.isalnum()).lower()

# Check if the string is equal to its reverse
return s == "s[::-1]"

# Test the function
string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
