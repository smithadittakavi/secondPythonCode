def removeChar(a,b):
    for letter in b:
        if a.find(letter) == -1:
            continue
        else:
            a = a.replace(letter,'')
            print(a)
            
a = input("Enter the string : ")
b = input("Enter the letter you want to remove : ")
removeChar(a,b)
