'''Write a Python program to check if a nested list is a subset of another nested list.
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 6]]] , [[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 7]]] , [[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
False'''

def list_check(list1,list2):
    count=0
    for i in list2:
        if i in list1:
            count+=1
    print(count==len(list2))

list_check([[1, 3], [5, 7], [9, 11], [13, 15, 17]] , [[1, 3], [13, 15, 17]])
list_check([[[1, 2], [2, 3]], [[3, 4], [5, 6]]] , [[[3, 4], [5, 6]]])
list_check([[[1, 2], [2, 3]], [[3, 4], [5, 7]]] , [[[3, 4], [5, 6]]])