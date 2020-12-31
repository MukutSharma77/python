#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.

# 2 list
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
print("List 1 is :  ",list1)
print("List 1 is :  ",list2)
#Checking each element of list 1 and the checking is it in list 2 if yes appending it

intersection=[]
for i in list1:
    if i in list2:
        intersection.append(i)

print("Intersection of list1 and list2 is :   ",intersection)
