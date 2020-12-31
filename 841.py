'''Combined Consecutive Sequence
Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
consecutive_combo([44, 46], [45]) ➞ True
'''

def consecutive_combo(lst1,lst2):
    lst3=lst1+lst2
    lst_=[i for i in range(min(lst3) , max(lst3)+1)]
    print(sorted(lst3)==lst_)


consecutive_combo([7, 4, 5, 1], [2, 3, 6])
consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])
consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])
consecutive_combo([44, 46], [45])
