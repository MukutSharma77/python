'''Create a function to calculate the determinant of a 2 * 2 matrix. The determinant of the following matrix is: ad - bc:
[[a, b], [c, d]]
Examples
calc_determinant([
  [1, 2],
  [3, 4]
]) ➞ -2'''


matrix=[
    [1,2],
    [3,4]
]

print((matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]) )