'''Sum of all Evens in a Matrix
Create a function that returns the sum of all even elements in a 2D matrix.
Examples
sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]) ➞ 6
// 2 + 4 = 6
sum_of_evens([
  [1, 1],
  [1, 1]
]) ➞ 0
sum_of_evens([
  [42, 9],
  [16, 8]
]) ➞ 66'''

mat=[
[42, 9],
  [16, 8]
 ]
tot=0
for i in mat:
    for j in i:
        if j %2==0:
            tot+=j

print(tot)