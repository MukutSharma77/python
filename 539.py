'''Solving Exponential Equations With Logarithms
Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.
Examples
solve_for_exp(4, 1024) ➞ 5
solve_for_exp(2, 1024) ➞ 10
solve_for_exp(9, 3486784401) ➞ 10'''

import math

num1=1024
num2=2

print(round(math.log(num1,num2)))