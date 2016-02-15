def findFactor(n):
    if n < 0 : 
        print("Cannot find factor for negative number")
    elif n == 0:
        print("Factor for 0 is itself.")
    else:
        for i in range(1,n+1):
            if n%i == 0:
                print(i)

n = int(input("Enter a number : "))
findFactor(n)
