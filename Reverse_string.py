def reverse_string(s):
    return s[: : -1]
user_input=input("Enter the string to be reversed:")
result=reverse_string(user_input)
print(f"The reversed string is {result}")