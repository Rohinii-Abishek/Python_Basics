def factorial(n):
    if n<0:
        return "Enter a positive number"
    result=1
    for i in range(1,n+1):
        result*=i
    return result
user_input=int(input("Enter a number whose factorial is to be found:"))
print(f"The factorial of {user_input} is {factorial(user_input)}")    