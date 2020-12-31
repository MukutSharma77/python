'''Extract Unique values dictionary values
The original dictionary is : {‘gfg’: [5, 6, 7, 8], ‘best’: [6, 12, 10, 8], ‘is’: [10, 11, 7, 5], ‘for’: [1, 2, 5]}
The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]'''


dict_= {
    'gfg' : [5, 6, 7, 8],
    'is' : [10, 11, 7, 5],
    'best' : [6, 12, 10, 8],
    'for' : [1, 2, 5]
}

lst_=[]
for i in dict_.values():
    for j in i:
        lst_.append(j)

print(list(set(lst_)))