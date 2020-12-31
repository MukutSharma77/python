#Please write assert statements to verify that every number in the list [2,4,6,8] is even

#List of even number range 1 to 10 with list comprehension
list_=[i for i in range(1,11) if i%2==0]
print("List is :   ",list_)

#Checking All the element in list is even or not
count_eve=0
for i in list_:
    if i % 2==0:
        count_eve+=1
    else:
        pass

if count_eve==len(list_):
    print("Yes all the element in the list is even")
else:
    print("No not all the element in list is even")