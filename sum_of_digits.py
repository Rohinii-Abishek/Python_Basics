def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total    
user_input=int(input("Enter the number whose sum of digits is to be found:"))
print(f"The sum of digits of {user_input} is {sum_of_digits(user_input)}")        