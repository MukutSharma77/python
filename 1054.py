''' Write a Python program to remove None value from a given list.
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]'''


lst_=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
output=[i for i in lst_ if i != None]
print(output)