'''Python program Square of matrix'''


row=int(input("Enter row :  "))
col=int(input("Enter Columns : "))
mat1=[[int(input(f"Enter Number [{j}][{i}]   :   ")) for i in range(col)] for j in range(row)]

mat_sq=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        mat_sq[i][j]=mat1[i][j] ** 2


for i in mat_sq:
    for j in i:
        print(j,end="   ")
    print()