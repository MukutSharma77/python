'''Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns  as input from the user.
Input rows: 2
Input columns: 2
1 2
3 4
sum for each column:
4 6'''

num_row=2
num_col=2
k=1
mat_=[[0 for i in range(num_col) ] for j in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        mat_[i][j]=k
        k+=1

print("Matrix is :  ")
for i in mat_:
    for j in i:
        print(j,end="  ")
    print()

print('\nSum of Columns :  ')
for i in range(num_row):
    tot=0
    for j in range(num_col):
        tot+=mat_[j][i]
    print(tot,end="     ")