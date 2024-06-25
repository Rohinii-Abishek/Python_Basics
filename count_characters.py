def count_characters(s):
    return len(s)
user_input=input("Enter the string whose characters are to be counted: ")
result=count_characters(user_input)
print(f"The number of characters in the {user_input} are {result}")