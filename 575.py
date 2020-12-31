'''Pythagoras Calculator
Create a function that will find the hypotenuse in a right angle triangle.
The pythagoras equation: a²+b²=c²
Examples
pythagoras(4, 3) ➞ 5  // 4²+3²=25, √25=5
pythagoras(5, 12) ➞ 13
Notes
Don't forget to use return. Use the math libary'''

import math

def pythagoras(num1,num2):
    sol=(num2**2) + (num1**2)
    print(int(math.sqrt(sol)))

num1=12
num2=5

pythagoras(num1,num2)