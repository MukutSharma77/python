# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

#Function to check element is even or not
def even_(num):
    if num % 2 == 0:
        return num
    else:
        pass



#List
list_=[1,2,3,4,5,6,7,8,9,10]

#using filter funtion in side the list() than printing it
list_eve=list(filter(even_,list_))
print(list_eve)