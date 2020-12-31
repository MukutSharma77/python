'''Find the Index (Part 1)
Create a function that finds the index of a given item.
Examples
search([1, 5, 3], 5) ➞ 1
search([9, 8, 3], 3) ➞ 2
search([1, 2, 3], 4) ➞ -1'''

list_=[1, 5, 3]
idx=4

if idx in list_:
    print(list_.index(idx))
else:
    print('-1')