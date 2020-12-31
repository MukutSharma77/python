'''
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5
'''

i=5
while i>=1:
    space=i-1
    while space>=1:
        print(' ',end=" ")
        space-=1
    j=i
    while j<=5:
        print(j,end=" ")
        j+=1
    print()
    i-=1


for i in range(5,0,-1):
    for space in range(i-1,0,-1):
        print(' ',end=" ")
    for j in range(i,6):
        print(j,end=" ")
    print()