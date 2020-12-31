#Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].list comprehension

#Inputting list
list_=[5,6,77,45,22,12,24]
print("List is :  ",list_)
#List comrehension element from list_ if it is not vene

list_=[i for i in list_ if i % 2 != 0]
print("Removed all even number from list :  ",list_)
