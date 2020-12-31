'''
  *
 * *
*   *
 * *
  *
'''

i=0
while i<=5:
    j=0
    while j<=5:
        if (i==0 and j==2) or (i==1 and (j==1 or j==3)) or i==2 and (j==0 or j==4) or i==3 and (j==1 or j==3) or (i==4 and j==2):
            print('*',end="")
        else:
            print(' ',end="")
        j+=1
    print()
    i+=1

print()


for i in  range(0,5):
    for j in range(0,5):
        if i+j==2 or j-i==2 or i+j==6 or i-j==2:
            print('*',end="")
        else:
            print(" ",end="")
    print()