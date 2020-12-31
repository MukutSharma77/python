'''
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5
'''
i=1
while i<=5:
    space=abs(1-i)
    while space>=1:
        print(" ",end=" ")
        space-=1
    j=i
    while j<=5:
        print(j,end=" ")
        j+=1
    print()
    i+=1

print()
for i in range(1,6):
    for space in range(i-1,0,-1):
        print(' ',end=" ")
    for k in range(i,6):
        print(k,end=" ")
    print()