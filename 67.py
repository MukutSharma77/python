#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def even(n):
    if n % 2 ==0:
        return n

def sq(n):
    return n**2

#List
list_=[1,2,3,4,5,6,7,8,9,10]

#First filtering all even number from list
ev_list=list(filter(even,list_))
print("All even number from list is :   ",ev_list)

#Now square of even number with the help of map
ev_list=list(map(sq,ev_list))
print("Square of even  number is :  ",ev_list)