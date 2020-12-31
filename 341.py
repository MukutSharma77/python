'''Cube the Square Root
Create a function that takes a number as an argument and returns the square root of that number cubed.
Examples
cube_squareroot(81) ➞ 729
'''

import math
num=int(input("Enter number :  "))
print("sqrt of a number is :   ",(math.sqrt(num)).__round__(2))
print("Cube of a squre root  ;  ",(math.sqrt(num)).__round__(2)**3)