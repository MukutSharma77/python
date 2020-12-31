'''Intersecting Intervals
Create a function that takes in a list of intervals and returns how many intervals overlap with a given point.
An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).
To illustrate:
count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
Examples
count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0
count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2
count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2'''

lst=[[1, 2], [5, 8], [6, 9]]
point=7
count=0
for i in lst:
    if i[0] <= point and i[1] >= point:
        count+=1

print(count)