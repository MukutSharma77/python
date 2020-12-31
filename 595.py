'''Nth Smallest Element
Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).
Examples
nth_smallest([1, 3, 5, 7], 1) ➞ 1
nth_smallest([1, 3, 5, 7], 3) ➞ 5
nth_smallest([1, 3, 5, 7], 5) ➞ None
nth_smallest([7, 3, 5, 1], 2) ➞ 3'''

lst=[7, 3, 5, 1]
num=5
if num<len(lst):
    lst.sort()
    print(lst[num-1])
else:
    print(None)