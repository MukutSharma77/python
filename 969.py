'''Write a Python program to get the depth of a dictionary.
dic = {'a':1, 'b': {'c': {'d': {}}}}
output:
4'''

dic = {'a':1, 'b': {'c': {'d': {}}}}
count_val=0


for i in dic:
    if i=='{' or i=='}':
        count_val+=1

print(count_val//2)