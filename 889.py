'''
10
10 8
10 8 6
10 8 6 4
10 8 6 4 2
'''

i=1
while i<=5:
    k=10
    j=1
    while j<=i:
        print(k,end=" ")
        k-=2
        j+=1
    print()
    i+=1

print()

for i in range(1,6):
    k=10
    for j in range(1,i+1):
        print(k,end=" ")
        k-=2
    print()