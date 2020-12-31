'''Write a Python program to reverse strings in a given list of string values.
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']'''


list_=['Red', 'Green', 'Blue', 'White', 'Black']
output=[i[::-1] for i in list_]
print(output)