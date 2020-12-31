'''Perfect Square Patch
Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.
Examples
square_patch(3) ➞ [
  [3, 3, 3],
  [3, 3, 3],
  [3, 3, 3]
]
square_patch(5) ➞ [
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5]
]
square_patch(1) ➞ [
  [1]
]
square_patch(0) ➞ []
Notes
n >= 0.
If n == 0, return an empty list'''


num=5
lst1=[num for i in range(num)]
lst_output=[lst1 for i in range(num)]
print(lst_output)