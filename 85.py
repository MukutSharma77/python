#Python Program to Sum All the Items in a Dictionary

#Craeting a dictionary
dictionary1={
    1 : 2,
    2 : 4,
    3 : 9,
    4 : 16
}

#Adding each items of a dict with the help of loop storing it in variable name : Tot
tot=0
for i in dictionary1.keys():
    # print(i)
    tot += i

print("The total of Item is :   ",tot)