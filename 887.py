'''
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1

    k=i-1
    while k>=1:
        print(k,end=" ")
        k-=1

    print()
    i+=1

print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")



    print()
