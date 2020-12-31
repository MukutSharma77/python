'''Case Insensitive Comparison
Write a function that validates whether two strings are identical. Make it case insensitive.
Examples
match("hello", "hELLo") ➞ True
match("motive", "emotive") ➞ False'''

def match(string1,string2):
    if string1==string2:
        print(True)
    else:
        print(False)



string1=input("Enter String1 :  ").lower()
string2=input("Enter String2 :  ").lower()
match(string1,string2)
