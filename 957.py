'''Write a Python program to remove key values pairs from a list of dictionaries.
Original List:
[{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
New List:
[{'key2': 'value2'}, {'key2': 'value4'}] '''


list_=[{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
lst2_output=[{key:val} for i in list_ for key,val in i.items() if key!='key1']

print(lst2_output)
