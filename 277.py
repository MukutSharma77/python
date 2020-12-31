'''his is a reverse coding challenge. Normally you're given explicit directions with how to create a function. Here, you must generate your own function to satisfy the relationship between the inputs and outputs.
Your task is to create a function that, when fed the inputs below, produce the sample outputs shown.
Examples
[5, 7, 8, 2, 1], 2 ➞ [1, 1, 0, 0, 1]
[9, 8, 16, 47], 4 ➞ [1, 0, 0, 3]
[17, 11, 99, 55, 23, 1], 5 ➞ [2, 1, 4, 0, 3, 1]
module
'''

def function(list_):
    no=int(input("Enter Number :  "))
    list2=[i%no for i in list_]
    print(list2)


list_=[9, 8, 16, 47]
function(list_)