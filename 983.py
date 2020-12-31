'''Write a Python program to create a multidimensional list (lists of lists) with zeros.
num_of_rows=3
num_of_column=2
output:
Multidimensional list: [[0, 0], [0, 0], [0, 0]]'''


num_of_rows=3
num_of_column=2
mat=[[0 for i in range(num_of_column)] for j in range(num_of_rows)]
print(mat)