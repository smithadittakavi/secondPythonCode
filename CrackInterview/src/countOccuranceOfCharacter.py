def countChar(string, letter):
    found = 0 
    for key in string:
        if key == letter:
            found = found+1
    return found

string = input("Enter string :")
letter = input("Letter to count: ")
print(countChar(string, letter))