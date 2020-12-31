'''Write a Python program to find the maximum and minimum values in a given heterogeneous list.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)'''

list_=['Python', 3, 2, 4, 5, 'version']
list_=[i for i in list_ if type(i)==int]
print((max(list_),min(list_)))