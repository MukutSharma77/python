'''Remove the First and Last Characters
Create a function that removes the first and last characters from a string.
Examples:
remove_first_last("hello") ➞ "ell"
remove_first_last("maybe") ➞ "ayb"
remove_first_last("benefit") ➞ "enefi"
remove_first_last("a") ➞ "a"
'''


string='benefit'

if len(string) < 3:
    print(string)
else:
    print(string[1:-1])