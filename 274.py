'''Return a List of Sublists
Write a function that takes three arguments (x, y, z) and returns a list containing x sublists (e.g. [[], [], []]), each containing y number of item z.
x Number of sublists contained within the main list.
y Number of items contained within each sublist.
z Item contained within each sublist.
Examples
matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
'''

def function(matrix):
    x,y,z=matrix
    matrix_output=[[z for col in range(y) ] for row in range(x)]
    print(matrix_output)


matrix=[2, 1, "edabit"]
function(matrix)