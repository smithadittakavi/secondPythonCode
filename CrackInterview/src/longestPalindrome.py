def find_char_backwards(a, c):
    for i in range(len(a) - 1, -1,-1):
        if a[i] == c:
            index=i
            return True, index

    return False, 0

def longest_palindorme(a):
    if len(a) < 2:
        return a
    else:
        c=a[0]
        (exist_char,index) = find_char_backwards(a[1:],c)
        if exist_char:
            palindrome=[c] + longest_palindorme(a[1:index+1]) + [c]
        else:
            palindrome=[]
        rest_palidorme=longest_palindorme(a[1:])

    if len(palindrome)>len(rest_palidorme):
        return palindrome
    else:
        return rest_palidorme
    
a = list(input("Enter a string : "))
print(longest_palindorme(a))
