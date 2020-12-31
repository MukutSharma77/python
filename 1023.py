'''Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
Original list:
[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
Range: 8 , 10
Sum of the specified range:
29'''

list_=[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
range_from=8
range_to=10
tot=0
for i in range(range_from,range_to+1):
    tot+=list_[i]
print(tot)