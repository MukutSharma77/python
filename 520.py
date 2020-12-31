'''The Museum of Incredibly DULL Things
Create a function that takes a list of integers and removes the smallest value.
Examples
remove_smallest([1, 2, 3, 4, 5] ) ➞ [2, 3, 4, 5]
remove_smallest([5, 3, 2, 1, 4]) ➞ [5, 3, 2, 4]
remove_smallest([2, 2, 1, 2, 1]) ➞ [2, 2, 2, 1]'''

list_=[5, 3, 2, 1, 4]
list_.remove(min(list_))
print(list_)