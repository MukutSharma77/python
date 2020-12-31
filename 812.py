'''Converting Dictionaries to Lists
Write a function that converts a dictionary into a list, where each element represents a key-value pair in the form of a list. Sort the list alphabetically by key.
Examples
to_list({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]
to_list({ "shrimp": 15, "tots": 12 }) ➞ [["shrimp", 15], ["tots", 12]]
to_list({}) ➞ []'''

def to_list(dict_):
    lst=[]
    for item , val in  dict_.items():
        lst.append([item,val])

    print(lst)


to_list({ "a": 1, "b": 2 })
to_list({ "shrimp": 15, "tots": 12 })
to_list({})