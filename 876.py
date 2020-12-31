'''
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''

i=6
while i>=1:
    j=i
    while j>=1:
        print('*',end=" ")
        j-=1
    print()
    i-=1


for i in range(6,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print()