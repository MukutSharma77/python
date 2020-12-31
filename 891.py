'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9

'''

i=1
k=1
while i<=5:
    j=1
    while j<=i:
        print(k,end=" ")
        j+=1
    print()
    k+=2
    i+=1

print()

k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end=" ")
    k+=2
    print()