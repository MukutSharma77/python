'''Sastry Numbers
In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not.
Examples
is_sastry(183) ➞ True
# Concatenation of n and its successor = 183184
# 183184 is a perfect square (428 ^ 2)
is_sastry(184) ➞ False
# Concatenation of n and its successor = 184185
# 184185 is not a perfect square
is_sastry(106755) ➞ True
# Concatenation of n and its successor = 106755106756
# 106755106756 is a perfect square (326734 ^ 2)
Notes
A perfect square is a number with a square root equals to a whole integer.'''

import math
num=106755
num_=int(str(num)+str(num+1))
sqrt_=math.sqrt(num_)
print(sqrt_.is_integer())
