'''Python program to input by user Matrices'''
row=int(input("Enter Number of rows :  "))
col=int(input("Enter Number of column :  "))
mat=[[int(input("Enter Number :  ")) for i in range(col)] for j in range(row)]

print("\nMatrix is :  ")
for i in mat:
    for j in i:
        print(j , end=" ")
    print()