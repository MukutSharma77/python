'''
Enter table number :  5
50  45  40  35
30  25  20
15  10
5

'''

table=int(input("Enter table number :  "))
i=4
k=10
while i>=1:

    j=1
    while j<=i:
        tab =table * k
        print(tab,end="  ")
        j+=1
        k-=1
    print()
    i-=1