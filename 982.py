''' Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110'''

list_=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
list_round=[round(i) for i in list_]

print('Mininmum value :  ',min(list_round))
print('Maximum value :  ',max(list_round))
list_=[i*5 for i in list_round]
list_.sort()
for i in list_:
    print(i,end="   ")