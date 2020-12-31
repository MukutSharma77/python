#Python Program to Replace all Occurrences of ‘a’ with $ in a String

string=input("Enter String :  ")

#Checking a present or not if present replacing it
if 'a' in string:
    string=string.replace('a','$')
else:
    print("a is not present")

print(string)