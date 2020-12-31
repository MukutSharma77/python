'''Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }'''

def mapping(list_):
    dict_={}
    for i in list_:
        dict_[i]=i.upper()
    print(dict_)

list_=["a", "b", "c"]
mapping(list_)