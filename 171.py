#Python Program to Search the Number of Times a Particular Number Occurs in a List

list_=[1,1,1,3,2,2,3,4,6,5,5,7,8,8]
list1=[]

for i in list_:
    if i not in list1:
        print(f"{i}    :     {list_.count(i) } times" )
        list1.append(i)