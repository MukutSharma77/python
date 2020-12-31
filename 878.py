'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i+=1


for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()