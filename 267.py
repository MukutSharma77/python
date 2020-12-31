'''Characters and ASCII Code Dictionary
Write a function that transforms a list of characters into a list of dictionaries, where:
The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
'''

dict_={ }

list_=["a", "b", "c"]

for i in list_:
    dict_[i]=ord(i)
print(dict_)