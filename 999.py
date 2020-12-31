'''Write a Python program to extract specified size of strings from a give list of string values.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']'''

list_=['Python', 'list', 'exercises', 'practice', 'solution']
length=8
list_output=[i for i in list_ if len(i)==length]
print(list_output)