''' Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
Original lists:
[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
Consecutive duplicate elements and their frequency:
([1, 2, 4, 5], [1, 3, 3, 4])'''

list_=[1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
list_set=list(set(list_))
print((list_set,[list_.count(i) for i in list_set]))