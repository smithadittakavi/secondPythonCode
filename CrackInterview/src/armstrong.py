def armstrong(a):
    s = 0
    temp = a 
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
    # display the result
    if a == s:
        print(a,"is an Armstrong number")
    else:
        print(a,"is not an Armstrong number")
        
a = int(input("Enter a number : "))
armstrong(a)
