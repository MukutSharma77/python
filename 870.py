'''
 * * * * *
  * * * *
   * * *
    * *
     *

'''


i=5
while i>=1:
    space=5
    j=i
    while space>=i:
        print(' ',end="")
        space-=1
    j=i
    while j>=1:
        print('*',end=" ")
        j-=1

    print()
    i-=1

print()
for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()