'''
1
3 2
6 5 4
10 9 8 7

'''

k=0
i=1
while i<=4:
    k+=i
    j=1
    while j<=i:
        print(k,end=" ")
        k-=1
        j+=1
    print()
    k+=i
    i+=1

print()

k=0
for i in range(1,5):
    k+=i
    for j in range(1,i+1):
        print(k,end=" ")
        k-=1
    print()
    k+=i