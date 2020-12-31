'''

Write a Python program to iterate over dictionaries using for loops.
Red corresponds to  1
Green corresponds to  2
Blue corresponds to  3
'''

colour={
    'Red' : 1,
    'Green' : 2,
    'Blue' : 3
}

for i , k in colour.items():
    print(i+' Corresponds to ',k)