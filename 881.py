'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1 
'''


i=5
while i>=1:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i-=1

print()
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()