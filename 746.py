'''Peeling off the Outer Layers
Given a list of lists, return a new list of lists containing every element, except for the outer elements.
Examples
peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["f", "g"],
  ["j", "k"]
]'''

lst=[
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]
mat=[]
for i in range(len(lst)):
    if i==0 or i==len(lst)-1:
        pass
    else:
        mat.append(lst[i][1:-1])

print(mat)