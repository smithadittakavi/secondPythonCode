def unique(s):
    c1 = set()
    for c in s:
        if c in c1:
            print(s," is not Unique")
            return False
        c1.add(c)
    print(s," is Unique")
    return True 

s = input("Enter a string : ")
s1 = unique(s)
print(s1)
        
        
        
        
# SECOND WAY F IMPLEMANTATION 
def unique1(s):
    if len(s) > 256:
        print("There is no uniqueness here")
        return False 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print("Since 2 strings are same, there is duplicate available")
            return False
    print("Since none of the char are equal, we found uniquness")
    return True

s = input("Enter a string : ")
s1 = unique1(s)
print(s1) 


# 3rd way of implemting it is : 

def isUniqueChars(string):
    
    checker = 0
    for c in string:
        val = ord(c) - ord('a')
        if (checker & (1 << val) > 0):
            return False
        else:
            checker |= (1 << val)
    return True
  
string = input("Enter a string :")
print(isUniqueChars(string))