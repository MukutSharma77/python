'''
list1=['M' , 'na' , 'i' , 'MUK']
list2=['y','me','s','UT']
output :
['My', 'name', 'is', 'MUKUT']
'''

list1=['M' , 'na' , 'i' , 'MUK']
list2=['y','me','s','UT']
lst3=[]
for i in range(len(list2)):
    lst3.append(list1[i]+list2[i])

print(lst3)