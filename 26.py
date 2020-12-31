'''wo digits m (row) and n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.'''

#Inputing two number row and column and 0 matrix of row*col
row=int(input("Enter number of row    :   "))
col=int(input("Enter number of columns:   "))

matrix=[[0 for i in range(col)] for j in range(row)]


#appendin i*j values

for i in range(row):
    for j in range(col):
        matrix[i][j]=i*j

for i in matrix:
    for j in i:
        print(format(j),end="  ")
    print()