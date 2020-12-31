'''Write a Python program to create a 3X3 grid with numbers.
3X3 grid with numbers:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]'''

num_of_row=3
num_of_col=3
mat=[[i for i in range(1,num_of_col+1)] for j in range(num_of_row)]
print(mat)