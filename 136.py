'''133)		Simple pattern printing programs in Python
1
2 3
4 5 6
7 8 9 10
11 12 13 14'''

#Entering number for how many rows J should print
num=int(input("Enter Number of rows   :   "))

#Using two loops or nested loop , one loop[ to to cahnge the row second loop to print the k and k is initilise by 1 increament is in loop
i=1
k=1


while i <= num:
   j=1
   while j<=i:
       print(k,end=" ")
       k+=1
       j+=1
   print()
   i+=1