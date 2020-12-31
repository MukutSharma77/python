#Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List


list1=[-1,-2,-3,4,5,6,7,8,9,10]
odd=0
ev=0
neg=0

for i in list1:
    if i >= 0:
        if i % 2==0:
            ev+=i
        elif i % 2!=0:
            odd+=i
    else:
        neg+=i


print("Sum of Positive even number :    ",ev)
print("Sum of Positive odd number :    ",odd)
print("Sum of Positive negitivw number :    ",neg)