def armstrong_number(n):
    digits=str(n)
    power=len(digits)
    sum_of_powers=0
    for i in digits:
        sum_of_powers +=int(i)**power 
    if sum_of_powers==n:
            return f"{n} is an Armstrong number"
    else:
            return f"{n} is not an Armstrong number"
user_input=int(input("Enter a number:")) 
print(armstrong_number(user_input))     

