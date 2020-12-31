'''
Enter table number :  5

5
10  15
20  25  30
35  40  45  50
'''

table=int(input("Enter table number :  "))
i=1
tab=table
while i<=4:
    j=1
    while j<=i:
        print(tab,end="  ")
        j+=1
        tab+=table
    print()
    i+=1