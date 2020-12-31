'''
Enter table number :  4
40
36  32
28  24  20
16  12  8  4
'''

table=int(input("Enter table number :  "))
i=1
k=10
while i<=4:

    j=1
    while j<=i:
        tab =table * k
        print(tab,end="  ")
        j+=1
        k-=1
    print()
    i+=1