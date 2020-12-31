'''
*
* *
* * *
* * * *
* * * * *

'''


i=1
while i<=5:
    j=1
    while j<=i:
        print('*',end=" ")
        j+=1
    print()
    i+=1


for i in range(6):
    for j in range(i):
        print('*',end=" ")
    print()