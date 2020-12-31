# Python program to print perfect numbers from the given list of integers

#Input list
list_=[2,3,4,6,28,8,9,10,496]


#Checking each element is it Perfect number
perfect=[]
for i in list_:
    tot=0
    for j in range(1,i):
        if i % j==0:
         tot+=j
        else:
            pass
    if tot==i:
        perfect.append(i)
    else:
        pass

print('Perfect number is :   ',end=' ')
for i in perfect:
    print(i,end="  ")