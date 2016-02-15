def palindrome(a):
    i = 0
    while i <= len(a):
        if a[i] == a[-1-i]:
            print("String is palindrom")
            return True
        print("String is NOT palindrome")
        return False

a = input("Enter the string : ")
palindrome(a)
