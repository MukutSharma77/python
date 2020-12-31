'''Check If Lines Are Parallel
Given two lines, determine whether or not they are parallel.
Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.
Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
# x+2y=3 and x+2y=4 are parallel.
'''

list1=[1, 2, 3]
list2=[1, 2, 4]


if -list1[0]/list1[1] == -list2[0]/list2[1]:
    print(True)
else:
    print(False)