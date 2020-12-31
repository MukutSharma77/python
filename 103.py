#Python Program to Find the Union of two Lists


#inputted two list
list1=[23, 15, 2, 14, 14, 16, 20 ,52]
list2 = [2, 48, 15, 12, 26, 32, 47, 54]
print("\nlist 1 is : ",list1)
print("\nlist 2 is : ",list2)
#concating it than removing duplicate value with set than again in list
list3=list(set(list2+list1))
print("\nIntersection of both the list is :  ",list3)