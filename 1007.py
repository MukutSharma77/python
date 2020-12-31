'''Write a Python program to access multiple elements of specified index from a given list.
Original list:
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Index list:
[0, 3, 5, 7, 10]
Items with specified index of the said list:
[2, 4, 9, 2, 1]'''

def idx_lst(lst,idx_lst):
    lst_output=[]
    for i in range(len(lst)):
        if i in idx_lst:
            lst_output.append(lst[i])

    print(lst_output)


idx_lst([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2] , [0, 3, 5, 7, 10])