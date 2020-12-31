''' Convert key-values list to flat dictionary
The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1, 2, 3]}
Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}'''


dict_= {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]}
list1_=dict_['name']
list2=dict_['month']
dict_output={}
for i in range(len(list2)):
    dict_output[list2[i]]=list1_[i]

print(dict_output)