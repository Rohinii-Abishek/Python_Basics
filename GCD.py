# Greatest Common Divisor
# GCD of two positive numbers is the greatest number which will divide both the numbers completely
# GCD of 12(1,2,3,4,6,12) & 14(1,2,7,14) is 2
# GCD  AKA HCF (Highest Common Factor)

def GCD(a,b):
    while b:
        a,b = b, a%b
    return a
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
result=GCD(n1,n2)
print(f"The GCD of {n1} and {n2} is {result}")