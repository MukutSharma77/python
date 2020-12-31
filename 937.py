'''
 Write a Python program to shuffle and print a specified list.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output : ['Yellow', 'Pink', 'Green', 'Red', 'Black', 'White']
'''

import random
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
random.shuffle(color)
print(color)