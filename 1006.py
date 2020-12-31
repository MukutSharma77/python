''' Write a Python program to find the item with maximum occurrences in a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Item with maximum occurrences of the said list:
2'''


lst_=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

max_occ=lst_[0]
for i in lst_:
    if lst_.count(i) > lst_.count(max_occ):
        max_occ=i

print(max_occ)