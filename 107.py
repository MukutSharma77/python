#Python Program to Find Element Occurring Odd Number of Times in a List

#list 1 to 10
list_=[1,2,3,4,5,6,7,8,9,10]

# counting if i is odd

odd=0
for i in list_:
    if i % 2 != 0:
        odd+=1

print("Total odd number :  ",odd)