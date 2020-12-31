i=6
while i>=1:
    space=6-i
    while space>=1:
        print(' ',end="")
        space-=1
    j=i
    while j>=1:
        print("*",end=" ")
        j-=1
    print()
    i-=1


i=1
while i<=6:
    space=6-i
    while space >= 1:
        print(" ",end="")
        space-=1
    j=1
    while j <= i:
        print('*',end=" ")
        j+=1
    print()
    i+=1



for i in range(6,-1,-1):
    for space in range(6,i,-1):
        print(' ',end="")
    for j in range(i):
        print('*',end=" ")
    print()

for i in range(1,7):
    for space in range(6,i,-1):
        print(' ',end="")
    for j in range(i):
        print('*',end=" ")
    print()