'''Invert Keys and Values
Write a function that inverts the keys and values of a dictionary.
Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }
invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }
invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }'''

dict_={ "zebra": "koala", "horse": "camel" }
dict_result={}
for key,val in dict_.items():
    dict_result[val]=key

print(dict_result)
