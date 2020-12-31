'''
Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd'''


data= {'1':['a','b'], '2':['c','d']}
lst1=data['1']
lst2=data['2']

for i in range(0,len(lst1)):
    for j in range(len(lst2)):
        k=[lst1[i],lst2[j]]
        print(''.join(k))