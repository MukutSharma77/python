'''
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
'''
i=1
while i<=6:
    space=6-i
    while space>=1:
        print(" ",end="")
        space-=1
    j=1
    while j<=i:
        print('*',end=" ")
        j+=1
    print()
    i+=1

print()

for i in range(1,7):
    for space in range(6-i,0,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end=" ")
    print()