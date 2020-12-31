'''Merge Lists in Order
Given two lists, merge them to one list and sort the new list in the same order as the first list.
Examples
merge_sort([1, 2, 3], [5, 4, 6]) ➞ [1, 2, 3, 4, 5, 6]
merge_sort([8, 6, 4, 2], [-2, -6, 0, -4]) ➞ [8, 6, 4, 2, 0, -2, -4, -6]
merge_sort([120, 180, 200], [190, 175, 130]) ➞ [120, 130, 175, 180, 190, 200]
Notes
You'll always get two lists as arguments.'''

lst1=[120, 180, 200]
lst2= [190, 175, 130]

if sorted(lst1)==lst1:
    print(sorted(lst1+sorted(lst2)))

elif sorted(lst1,reverse=True)==lst1:
    print(lst1+sorted(lst2,reverse=True))
else:
    pass