'''Write a Python program to insert an element before each element of a list.
Original List:  ['Red', 'Green', 'Black']
Output_List:  ['c', 'Red', 'c', 'Green', 'c', 'Black'] '''

lst= ['Red', 'Green', 'Black']
lst_output=[ ]

for i in lst:
    lst_output.append('c')
    lst_output.append(i)

print(lst_output)