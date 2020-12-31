#By using list comprehension, please write a program to print the list after removing the
# 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

#list

list_= [12,24,35,70,88,120,155]



#List slicing to dis[play only odd index element

list_=list_[1::2]

print("List after removing given index :   ",list_)
