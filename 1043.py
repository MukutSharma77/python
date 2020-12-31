'''Write a Python program to reverse a given list of lists.
reverse( [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']] )
reverse( [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]] )
Output :
[['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
[[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]'''

def reverse(lst_):
    print(lst_[::-1])


reverse( [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']] )
reverse( [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]] )