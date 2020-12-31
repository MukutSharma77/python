# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

def sq(n):
    return  n**2


#list
list_=[1,2,3,4,5,6,7,8,9,10]

#using filter to do sq of each element from list_

sq_list=list(map(sq,list_))
print('Square of list : ',sq_list)