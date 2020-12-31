'''Transpose a matrix'''

row=int(input("Enter row of matrix :  "))
col=int(input("Enter column of matrix :  "))

mat=[[int(input("Enter Number :   ")) for i in range(col)] for j in range(row)]

for i in mat:
    for j in i:
        print(j,end="  ")
    print()

transpose=[[0 for i in range(row)] for j in range(col)]

for i in range(row):
    for j in range(col):
        transpose[j][i]=mat[i][j]


print("Transpose of matrix :  ")

for i in transpose:
    for j in i:
        print(j, end="  ")
    print()
