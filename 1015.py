''' Write a Python program to create a list taking alternate elements from a given list.
alternate(['red', 'black', 'white', 'green', 'orange'])
alternate([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])
Output :
['red', 'white', 'orange']
[2, 3, 0, 8, 4]'''

def alternate(lst):
    lst_output=[lst[i] for i in range(0,len(lst) , 2)]
    print(lst_output)


alternate(['red', 'black', 'white', 'green', 'orange'])
alternate([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])
