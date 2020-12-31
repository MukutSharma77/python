'''Product of a diagnol of a input matrix'''

row=int(input("Enter row of matrix :  "))
col=int(input("Enter column of matrix :  "))

mat=[[int(input("Enter Number :   ")) for i in range(col)] for j in range(row)]

for i in mat:
    for j in i:
        print(j,end="  ")
    print()

print()
print("Product of diagnol :   ",end=" ")
product=1
for i in range(row):
    for j in range(col):
        if i==j:
            product*=mat[i][j]


print(product)