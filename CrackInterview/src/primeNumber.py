def prime(a):
    if a == 2: 
        print(a," is Prime")
    elif (a % 2 == 0):
        print(a," is NOT prime")
    else:
        print(a," is Prime")
        
a = int(input("Enter number to check : "))
prime(a)
