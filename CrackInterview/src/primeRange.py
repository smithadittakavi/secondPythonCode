lower = int(input('Enter Lower Limit : '))
upper = int(input("Enter upper limit : "))
for num in range(lower, upper+1):
    if num >= 2:
        prime = True
        for i in range(2,num):
            if (num % i == 0):
                prime = False
        if prime:
            print(num)