#Python Program to Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1

list_=[10,20,30,40,50]
print("List is :    ",list_)

list2=[ ]

for i in range(0,len(list_)):
    tot=0
    for j in range(0,i+1):
        tot+=list_[j]
    list2.append(tot)


print(list2)