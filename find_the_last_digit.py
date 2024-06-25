def last_digit(n):
    result=n%10
    return result
user_input=int(input("Enter a number whose last digit is to be found"))
print(f"The last digit of {user_input} is {last_digit(user_input)}")