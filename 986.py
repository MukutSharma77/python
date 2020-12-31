''' Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal:
14'''

num_of_row=3
num_of_col=3
mat=[[int(input('>   ')) for i in range(num_of_col)] for j in range(num_of_row)]

print()
print("Matrix is :    ")
for i in mat:
    for j in i:
        print(j,end="  ")
    print()

print()
tot=0
print('Sum of diagnol  :   ',end=" ")
for i in range(num_of_row):
    for j in range(num_of_col):
        if i==j:
            tot+=mat[i][j]

print(tot)