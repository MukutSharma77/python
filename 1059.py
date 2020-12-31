'''Write a Python program to convert a tuple to a dictionary.
tuplex = ((2, "w"),(3, "r"))
output:
{'w': 2, 'r': 3}'''


tuplex = ((2, "w"),(3, "r"))
dict_={}
for i in tuplex:
    dict_[i[1]]=i[0]

print(dict_)