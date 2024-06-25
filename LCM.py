# The Least Common Multiple (LCM) of two numbers is the smallest positive integer 
# that is divisible by both of the given numbers without leaving a remainder
# Let's find the LCM of 4 and 6.
#The multiples of 4 are: 4, 8, 12, 16, 20, ...
#The multiples of 6 are: 6, 12, 18, 24, ...
# So, the LCM of 4 and 6 is 12.

def GCD(a,b):
    while b:
        a,b=b,a%b
    return a
def LCM(a,b):
    return (a*b)//GCD(a,b)
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
result=LCM(n1,n2)
print(f"The LCM of {n1} and {n2} is {result}")
    
