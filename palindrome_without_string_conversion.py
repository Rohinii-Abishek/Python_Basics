def is_palindrome(n):
    original_number=n
    reversed_number=0
    while n>0:
        digit=n%10
        reversed_number= (reversed_number*10) + digit
        n//=10

    if reversed_number==original_number:
       return True
    else:
       return False

user_input=int(input("Enter a number:"))    
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome number")   
else:
   print(f"{user_input} is not a palindrome number")    