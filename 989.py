'''Write a Python program to find the list with maximum and minimum length.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''

def lst_max(lst):
    max_=lst[0]
    min_=lst[0]
    for i in lst:
        if len(i) > len(max_):
            max_=i

        elif len(i) < len(min_):
            min_=i

    print((len(max_),max_))
    print((len(min_),min_))


lst_max([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
