# Python Program to Remove the Duplicate Items from a List

#list
list_=[1,2,3,3,2,1,4,6,6,4,3,8,7,9,10]
print("List is :  ",list_)
uni_list=[]

for i in list_:
    if i not in uni_list:
        uni_list.append(i)


print("Unique elements are   :   ",uni_list)