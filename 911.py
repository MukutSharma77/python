'''
5 4 3 2 1
  4 3 2 1
    3 2 1
      2 1
        1
'''

i=5
while i>=1:
    space=5-i
    while space >=1:
        print(' ',end=" ")
        space-=1
    j=i
    while j>=1:
        print(j,end=" ")
        j-=1
    i-=1
    print()

print()
for i in range(5,0,-1):
    for space in range(5-i,0,-1):
        print(' ',end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()