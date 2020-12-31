'''Write a Python program to convert a given list of strings and characters to a single list of characters. Go to the editor
Original list:
['red', 'white', 'a', 'b', 'black', 'f']
Convert the said list of strings and characters to a single list of characters:
['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']'''

lst_=['red', 'white', 'a', 'b', 'black', 'f']
lst_output=[j for i in lst_ for j in i]
print(lst_output)