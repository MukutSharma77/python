'''
256)
Create a function that returns the indices of all occurrences of an item in the list.
Examples
get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
get_indices([1, 5, 5, 2, 7], 7) ➞ [4]
get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]
'''

def function(list_):
    search=input("Search from list :  ")
    idx=[]
    count=0
    if search.isdigit():
       if int(search) in list_:
            for i in list_:
                if i==int(search):
                    idx.append(count)
                    count += 1
                else:
                    count += 1
            print(idx)



    else:
        if search in list_:

            for i in list_:
                if i == search:
                    idx.append(count)
                    # list_.remove(i)
                    count += 1
                else:
                    count += 1
            print(idx)


list_=  ["a", "a", "b", "a", "b", "a"]
print(list_)
function(list_)