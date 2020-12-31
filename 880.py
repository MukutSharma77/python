'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''



i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()