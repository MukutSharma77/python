#By using list comprehension, please write a program to print the list after
# removing the value 24 in [12,24,35,24,88,120,155].list comprehension

#list
list_=[12,24,35,24,88,120,155]

#List comprehision
list_=[i for i in list_ if i != 24]
print("List is :   ",list_)
