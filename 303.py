'''Multiplying Numbers in a String
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0'''

number=input("Enter Number commo seprated :  ").split(",")
product=1
for i in number:
    product*=int(i)

print(product)