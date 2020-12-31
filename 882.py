'''
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5 '''


num=5
i=5

while num>=1:
    j=1
    while j <=num:
        print(i,end=" ")
        j+=1
    print()
    num-=1

print()

num=5
i=5

for k in range(num,0,-1):
    for j in range(1,k+1):
        print(i,end=" ")
    print()