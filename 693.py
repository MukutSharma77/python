'''Automorphic Numbers
A number n is automorphic if n^2 ends in n.
For example: n=5, n^2=25
Create a function that takes a number and returns True if the number is automorphic, False if it isn't.
Examples
is_automorphic(5) ➞ True
is_automorphic(8) ➞ False
is_automorphic(76) ➞ True
'''

num=76
sq=num**2
num=str(num)
sq=str(sq)
print(sq[len(num):]==num)