'''Rotate a Matrix 90 Degrees Clockwise
Create a function that receives a square n*n matrix and returns that matrix after it has been rotated 90 degrees in the clockwise direction.
Examples
rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
rotate([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["m", "i", "e", "a"],
  ["n", "j", "f", "b"],
  ["o", "k", "g", "c"],
  ["p", "l", "h", "d"]
]
'''
import numpy
def rotate(mat):
    # print(len(mat))
    mat_output=[[0 for i in range(len(mat))] for j in range(len(mat))]

    for i in range(len(mat)):
        for j in range(0,len(mat)):
            mat_output[i][j]=mat[j][i]

    for i in mat_output:
        i.reverse()
        print(i)


rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
rotate([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
])