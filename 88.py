# Python Program to Find the Largest Number in a List


#Inputting list
list_=[1,2,3,4,5,10,9,8,7,6]

#Assuming that 1 menas the index[0] is that is largest

max=list_[0]

#checking each value is it greater than idx[0] if yes than assigning it
for i in list_:
    if max < i:
        max=i

print("The largest value is :    ",max)