'''False
None
0
[]
{}
""
Create a function that takes an argument of any data type and returns 1 if it's truthy and 0 if it's falsy.
Examples
is_truthy(0) ➞ 0
is_truthy(False) ➞ 0
is_truthy("") ➞ 0
is_truthy("False") ➞ 1
'''

string=input("Enter datatype  :   ")
if string=='0' or string==False or string=="" or string=='False':
    print(0)
else:
    print(1)