'''
        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *
'''

i=1
while i<=5:
    space=5-i
    while space>=1:
        print(" ",end=" ")
        space-=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1


i=4
while i>=1:
    space=5-i
    while space>=1:
        print(" ",end=" ")
        space-=1
    j=i
    while j>=1:
        print('*',end=" ")
        j-=1
    print()
    i-=1



print()
print()

for i in range(1,6):
    for space in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i):
        print('*',end=" ")

    print()


for i in range(4,-1,-1):
    for space in range(5,i,-1):
        print(' ',end=" ")
    for j in range(1,i+1):
        print('*',end=" ")
    print()