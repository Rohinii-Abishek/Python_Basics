def reverse_number(n):
    reversed_num=0
    while n>0:
      remainder=n%10
      reversed_num=(reversed_num*10)+remainder
      n= n//10
    return reversed_num
user_input=int(input("Enter the number whose digits are to be reversed:"))
print(f"The reversed digits of {user_input} are {reverse_number(user_input)}")

