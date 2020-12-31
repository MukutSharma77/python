'''Python program to Subtarct two Matrices'''

print("Both row and column will be same")
row=int(input("Enter row :  "))
col=int(input("Enter Columns : "))
mat1=[[int(input(f"Enter Number [{j}][{i}]   :   ")) for i in range(col)] for j in range(row)]
print('\nMatrix 2 : ')
mat2=[[int(input(f"Enter Number [{j}][{i}]   :   ")) for i in range(col)] for j in range(row)]
print()
mat_add=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        mat_add[i][j]=mat1[i][j] - mat2[i][j]


for i in mat_add:
    for j in i:
        print(j,end="   ")
    print()