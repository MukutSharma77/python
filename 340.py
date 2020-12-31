'''Create a function to count the number of 1s in a 2D list.
Examples
count_ones([
  [1, 0],
  [0, 0]
]) ➞ 1
count_ones([
  [1, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]) ➞ 7'''


def count_ones(matrix):
    count=0
    for i in matrix:
        for j in i:
            if j==1:
                count+=1
    print(count)


matrix=[
  [1, 1, 1],
  [0, 0, 1],
  [1, 1, 1]]
count_ones(matrix)

