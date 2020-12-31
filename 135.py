'''133)		Simple pattern printing programs in Python
1
1  2
1  2  3
1  2  3  4
1  2  3  4  5'''

#Entering number for how many rows J should print
num=int(input("Enter Number of rows   :   "))

#Using two loops or nested loop , one loop[ to to cahnge the row second loop to print the j
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()