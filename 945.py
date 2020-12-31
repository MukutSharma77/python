'''
Write a Python program to create multiple lists than add it all in dictionary with there numbers :
n=20
{'1': [], '8': [], '14': [], '5': [], '17': [], '9': [], '2': [], '7': [], '16': [], '19': [], '4': [], '18':
[], '13': [], '3': [], '15': [], '11': [], '20': [], '6': [], '12': [], '10': []}
'''

n=20
list_=[[] for i in range(n)]

dict_={ }
for i in range(0,n):
    dict_[str(i+1)]=list_[i]

print(dict_)