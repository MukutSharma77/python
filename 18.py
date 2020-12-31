#Print an Identity Matrix

#Inputing Row and col value it should be same
row=3
col=3

#Creating zero  matrix  of Row * Col

matrix=[[0 for i in range(col)] for j in range(row)]

#using loop for making identiy matrix from zero matrix
k=0
for i in range(row):
    for j in range(col):
        if k == j:
            matrix[i][j]=1

        else:
            matrix[i][j] = 0

    k += 1


for i in matrix:
    for j in i:
        print(j,end=" ")
    print()