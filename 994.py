'''Write a Python program to sort a given list of lists by length and value.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]'''


list_=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
list_.sort()
list_.sort(key=len)
print(list_)