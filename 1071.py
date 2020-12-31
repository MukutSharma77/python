'''2-D matrix to 1-D matrix'''

mat_=[[1,2,3],[4,5,6],[7,8,9]]
mat_1d=[j for i in mat_ for j in i]
print(mat_1d)