'''Multiply Every List Item by Two
Create a function that takes a list with numbers and return a list with the elements multiplied by two.
Examples
get_multiplied_list([2, 5, 3]) ➞ [4, 10, 6]
get_multiplied_list([1, 86, -5]) ➞ [2, 172, -10]'''

def get_multiplied_list(list_):
    list2=[]
    for i in list_:
        list2.append(i*2)
    return list2


list_=[2, 5, 3]
result=get_multiplied_list(list_)
print(result)