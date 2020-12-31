'''Write a Python program to find a tuple, the smallest second index value from a list of tuples.
x = [(4, 1), (1, 2), (6, 0)]
Output:
(6, 0)
'''
x = [(4, 1), (1, 2), (6, 0)]
x.sort(key=lambda  e:e[-1])
print(x[0])