def factorial(n):
    fact = 1
    if n < 0 : 
        print("Factorial for negative numbers doesn't exist")
    elif n == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact = fact*i
        print('Factorial of ',n,' is ',fact)

n = int(input("enter a number : ")) 
factorial(n)           