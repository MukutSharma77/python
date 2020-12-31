''' Write a Python program to sort a list of nested dictionaries.
Original List:
[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
Sorted List:
[{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]  '''

lst=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

lst.sort(key=lambda  e : e['key']['subkey'] , reverse=True)
print(lst)
