'''Return Duplicate Numbers
Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list.
Examples
duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]
duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]
duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None
Notes
The given list won't contain the same number three times'''

lst=[1, 2, 3, 4, 3, 5, 6]
dup=[]

for i in lst:
    if lst.count(i)>1:
        dup.append(i)

if dup:
    print(sorted(list(set(dup))))
else:
    print(None)