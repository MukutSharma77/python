'''133)		Simple pattern printing programs in Python
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *'''

#Entering number for how many rows star should print
num=int(input("Enter Number of rows   :   "))

#Using two loops or nested loop , one loop[ to to cahnge the row second loop to print the stars
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
