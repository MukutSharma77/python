'''
     1
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
6 6 6 6 6 6
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
     1
'''

i=1
while i<=6:
    space=6-i
    while space >=1:
        print(' ',end="")
        space-=1
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i+=1

i=5
while i>=1:
    space=6-i
    while space>=1:
        print(' ',end="")
        space-=1

    j=i
    while j>=1:
        print(i,end=" ")
        j-=1
    print()
    i-=1


print()
print()

for i in range(1,7):
    for space in range(6-i,0,-1):
        print(' ',end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

for i in range(5,0,-1):
    for space in range(6-i,0,-1):
        print(' ',end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()