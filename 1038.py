'''Write a Python program to extract every first or specified element from a given two-dimensional list.
Original list of lists:
extract( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]] , 1 )
extract( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]] , 3 )
Output
[1, 4, 7]
[3, 6, 9]'''

def extract(lst , idx):
    idx_lst=[]
    for i in lst:
        for j in range(len(i)):
            if j==idx-1:
                idx_lst.append(i[j])

    print(idx_lst)

extract( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]] , 1 )
extract( [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]] , 3 )
