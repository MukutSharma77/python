'''Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10'''

def function(list_):
    list_original=[i for i in range(1,11)]

    for i in list_original:
        if i not in list_:
            print(i,end="  ")


list_=[1, 2, 3, 4, 6, 7, 8, 9, 10]
function(list_)