'''Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})'''

lst=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

dict_={}


for i in range(len(lst)):
    count = 0
    for j in lst[i+1:]:
        if lst[i]['item']==j['item']:
            dict_[lst[i]['item']]=lst[i]['amount'] +j['amount']


for i in lst:
    for k,v in i.items():
        if i['item'] not in dict_.keys():
            dict_[v]=i['amount']
print(dict_)