'''Check if a String Contains only Identical Characters
Write a function that returns True if all characters in a string are identical and False otherwise.
Examples
is_identical("aaaaaa") ➞ True
is_identical("aabaaa") ➞ False
is_identical("ccccca") ➞ False'''


string=input("Enter String :  ")
if string.count(string[0]) == len(string):
    print(True)

else:
    print(False)