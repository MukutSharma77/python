'''Multiplying Numbers in a String
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20
'''

string="54, 75, 453, 0".split(',')
tot=1
for i in string:
    tot*=int(i)

print(tot)