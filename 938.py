'''
Write a Python program to generate and print a list except for the first 5 elements,
 where the values are square of numbers between 1 and 20 (both included).
'''

list=[i**2 for i in range(1,21)]
print(list[5:])