'''Alphanumeric Restriction
Create a function that returns True if the given string has any of the following:
Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters, or contains characters which don't fit into any category, return False
Examples
alphanumeric_restriction("Bold") ➞ True
alphanumeric_restriction("123454321") ➞ True
alphanumeric_restriction("H3LL0") ➞ False
alphanumeric_restriction("ed@bit") ➞ False
'''

string="ed@bit"
if string.isalpha():
    print(True)
elif string.isdigit():
    print(True)
else:
    print(False)