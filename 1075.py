''' sort list of dictionaries by values in Python
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }] '''
from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

lis.sort(key=itemgetter('age'))
print(lis)


lis.sort(key=itemgetter('name'))
print(lis)


lis.sort(key=itemgetter('age' , 'name'))
print(lis)