'''
Write a Python program to find missing and additional values in two lists.
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
Output :
Missing values in second list:  b,c,a
Additional values in second list:  g,h '''

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
uni=[]

for i in list1:
    if i not in list2:
        uni.append(i)

print("Missing Value is :  ",', '.join(uni))

advance=[]

for i in list2:
    if i not in list1:
        advance.append(i)
print('Advanced value is :   ',', '.join(advance))