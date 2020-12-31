'''
Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]
'''

def function(string):
    list_=[]
    for i in string:
        if i.isupper():
            list_.append(string.index(i))
        else:
            pass

    if list_:
        print(list_)
    else:
        print("No Cap")


string="eDaBiT"
function(string)