'''Write a Python program to remove empty lists from a given list of lists.
Original list:
[[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
After deleting the empty lists from the said lists of lists
['Red', 'Green', [1, 2], 'Blue']'''

lst=[[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
output=[]
for i in lst:
    if type(i)==list and len(i) > 1:
        output.append(i)
    elif type(i)==str or type(i)==int:
        output.append(i)
print(output)