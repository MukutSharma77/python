'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

'''


i=1
while i<=5:
    j=6-i
    while j>=1:
        print(i,end=" ")
        j-=1
    print()
    i+=1

print()

for i in range(1,6):
    for j in range(6-i,0,-1):
        print(i,end=" ")
    print()