'''Is the Number a Repdigit
A repdigit is a positive number composed out of the same digit. Create a function that takes an integer and returns whether it's a repdigit or not.
Examples
is_repdigit(66) ➞ True
is_repdigit(0) ➞ True
is_repdigit(-11) ➞ False'''

num=-11

if num>=0:
    num=str(num)
    print(len(num)==num.count(num[0]))
else:
    print(False)