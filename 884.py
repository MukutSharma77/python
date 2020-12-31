'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''

i=5
while i>=1:
    j=0
    while j <= i:
        print(j,end=" ")
        j+=1
    print()
    i-=1
print()
for i in range(5,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print()