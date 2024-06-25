# fibonacci function as a generator function
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib_gen = fibonacci()
for i in range(10):
    print(next(fib_gen))

# fibonacci series in general
fibonacci_series= []
def fibonacci(n):
    if n<0:
        return "please enter a positive number"
    elif n==0:
        return 0
    elif n==1:
        return 1
    fibonacci_series =[0,1]
    for i in range(2,user_input+1):
        next_number=fibonacci_series[i-1]+fibonacci_series[i-2]
        fibonacci_series.append(next_number)
    return fibonacci_series
user_input=int(input("Enter the number:"))   
result = fibonacci(user_input) \
