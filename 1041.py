'''Write a Python program to remove specific words from a given list.
Original list:
['red', 'green', 'blue', 'white', 'black', 'orange']
Remove words:
['white', 'orange']
After removing the specified words from the said list:
['red', 'green', 'blue', 'black']'''

lst_=['red', 'green', 'blue', 'white', 'black', 'orange']
remove_=['white', 'orange']
output=[i for i in lst_ if i not in remove_]
print(output)