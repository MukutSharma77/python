'''Matrix Transpose
In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; that is, it switches the row and column indices of the matrix A by producing another matrix, often denoted by A^T.
Create a function that takes a 2D matrix m and returns a 2D matrix (matrix A^T).
Examples
makeTranspose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
makeTranspose([
  [1, 2],
  [3, 4],
  [5, 6]
]) ➞ [
  [1, 3, 5],
  [2, 4, 6]
]
makeTranspose([
  ["a", "b"]
]) ➞ [
  ["a"],
  ["b"]
]
'''



def makeTranspose(mat):

    col=0
    row=0
    for i in mat:
        row+=1
        col=len(i)

    mat_output = [[0 for i in range(row)] for j in range(col)]

    for i in range(row):
        for j in range(col):
            mat_output[j][i]=mat[i][j]

    print(mat_output)

makeTranspose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
makeTranspose([
  [1, 2],
  [3, 4],
  [5, 6]
])
makeTranspose([
  ["a", "b"]
])