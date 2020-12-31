#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)


tuple_=(1,2,3,4,5,6,7,8,9,10)

#Even values from tuple in new tuple with the help of For Loop

new_tup=[]

for i in tuple_:
    if i % 2 == 0:
        new_tup.append(i)

new_tup=tuple(new_tup)
print("Even values from Tupple is :   ",new_tup)

