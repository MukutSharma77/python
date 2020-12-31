'''Write a Python program to insert an element at a specified position into a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
kth=2
value=12
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1]
'''


list_=[1, 1, 2, 3, 4, 4, 5, 1]
kth=2
value=12
list_.insert(kth,value)
print(list_)