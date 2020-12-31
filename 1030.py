''' Write a Python program to iterate over all pairs of consecutive items in a given list.
Original lists:
[1, 1, 2, 3, 3, 4, 4, 5]
Iterate over all pairs of consecutive items of the said list:
[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]'''

list_=[1, 1, 2, 3, 3, 4, 4, 5]
output=[]
for i in range(1,len(list_)):
    output.append((list_[i-1] , list_[i]))
print(output)