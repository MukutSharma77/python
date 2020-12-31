'''133)		Simple pattern printing programs in Python
1
1  1
1  1  1
1  1  1  1
1  1  1  1  1'''

#Entering number for how many rows star should print
num=int(input("Enter Number of rows   :   "))

#Using two loops or nested loop , one loop[ to to cahnge the row second loop to print the 1
i=1
while i<=num:
    j=1
    while j<= i:
        print("1",end=" ")
        j+=1
    print()
    i+=1