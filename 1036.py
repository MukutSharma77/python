'''Write a Python program to sum a specific column of a list in a given list of lists.
Original list of lists:
sum_( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] , 1 )
sum_( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] , 2 )
sum_( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] , 4 )
Output:
12
15
9'''

def sum_(list_,idx):
    tot=0
    for i in list_:
        for j in range(len(i)):
            if j==idx-1:
                tot+=i[j]

    print(tot)

sum_( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] , 1 )
sum_( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] , 2 )
sum_( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] , 4 )
