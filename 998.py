''' Write a Python program to sort a given matrix in ascending order according to the sum of its rows. Go to the editor
check([[1, 2, 3], [2, 4, 5], [1, 1, 1]])
check([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])
output:
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]'''

def check(lst):
    lst.sort(key=lambda e:sum(e))
    print(lst)
check([[1, 2, 3], [2, 4, 5], [1, 1, 1]])
check([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])
