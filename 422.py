'''Omnipresent Value
A value is omnipresent if it exists in every sublist inside the main list.
To illustrate:
[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
# 3 exists in every element inside this list, so is omnipresent.
Create a function that determines whether an input value is omnipresent for a given list.
Examples
is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ True
is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ False
is_omnipresent([[5], [5], [5], [6, 5]], 5) ➞ True'''

list_=[[5], [5], [5], [6, 5]]
no=5
count=0
for i in list_:
    for j in i:
        if j == no:
            count+=1
            break

if len(list_)==count:
    print(True)
else:
    print(False)