''' Write a Python program to join two given list of lists of same length, element wise.
join_( [[10, 20], [30, 40], [50, 60], [30, 20, 80]] , [[61], [12, 14, 15], [12, 13, 19, 20], [12]] )
join_([['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]  , [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']] )
Output:
[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
[['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]'''

def join_(lst , lst2):
    output=[]
    for i in range(len(lst)):
        output.append(lst[i] + lst2[i])
    print(output)

join_( [[10, 20], [30, 40], [50, 60], [30, 20, 80]] , [[61], [12, 14, 15], [12, 13, 19, 20], [12]] )
join_([['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]  , [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']] )
