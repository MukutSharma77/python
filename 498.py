'''Xs and Os, Nobody Knows
Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.
Return a boolean value (True or False).
The string can contain any character.
When no x and no o are in the string, return True.
Examples
XO("ooxx") ➞ True
XO("xooxx") ➞ False
XO("ooxXm") ➞ True
# Case insensitive.
XO("zpzpzpp") ➞ True
# Returns True if no x and o.
XO("zzoo") ➞ False
'''

string="zzoo".lower()

if string.count('x')==string.count('o') or (string.count('x') ==0 and string.count('o')==0):
    print(True)
else:
    print(False)
