'''Given a square matrix (i.e. same number of rows as columns), its trace is the sum of the entries in the main diagonal (i.e. the diagonal line from the top left to the bottom right).

As an example, for:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
... the trace is 1 + 5 + 9 = 15.

Write a function that takes a square matrix and computes its trace.
'''

matrix=[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

row=0
col=0
for i in matrix:
    for j in i:
        col+=1
    row+=1
print("Total number :   ",row)
print("Total number of col  ",col//row)



tot=0
for i in range(row):
    for j in range(j):
        if i == j:
            tot+=matrix[i][j]
print(tot)