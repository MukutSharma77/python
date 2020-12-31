'''Write a function that takes a list of elements and returns only the integers.
Examples
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
'''

def function(list):
    int_list=[]

    for i in list:
        i=str(i)
        if i.isdigit():
            int_list.append(int(i))

    print(int_list)




list=[9, 2, "space", "car", "lion", 16,5.6]
function(list)