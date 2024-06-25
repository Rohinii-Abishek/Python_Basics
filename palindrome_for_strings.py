def is_palindrome(s):
    s=s.lower()
    s=s.replace(" ","")
    start=0
    end=len(s)-1
    while start<end:
       if s[start] != s[end]:
        return False
    start+=1
    end-=1
    return True

user_input=input("Enter the string to check:")
if is_palindrome(user_input):
    print(f"{user_input} is palindrome")
else:
    print(f"{user_input} is not a palindrome")    

