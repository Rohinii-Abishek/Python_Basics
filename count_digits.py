def count_digits(n):
    return len(str(n))
user_input=int(input("Enter the nuber whose length is to be found"))
print(f"The count of {user_input} is {count_digits(user_input)}")