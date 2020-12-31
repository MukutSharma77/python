'''Concatenate Variable Number of Input Lists
Create a function that concatenates n input lists, where n is variable.
Examples
concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]
concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]'''


def concat(*args):
    lst2=[]
    for i in args:
        for j in i:
            lst2.append(j)
    print(lst2)

    
concat([1, 2, 3], [4, 5], [6, 7])
concat([1], [2], [3], [4], [5], [6], [7])
concat([1, 2], [3, 4])
concat([4, 4, 4, 4, 4])