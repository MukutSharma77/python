'''Check if the Same Case
Create a function that returns True if an input string contains only uppercase or only lowercase letters.
Examples
same_case("hello") ➞ True
same_case("HELLO") ➞ True
same_case("Hello") ➞ False
'''

def same_case(string):
    if string.isupper() or string.islower():
        print(True)
    else:
        print(False)


string='hello'
same_case(string)