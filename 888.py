'''
5 4 3 2 1 1 2 3 4 5
5 4 3 2 2 3 4 5
5 4 3 3 4 5
5 4 4 5
5 5
'''

i=1
while i<=5:
    j=5
    while j>=i:
        print(j,end=" ")
        j-=1
    k=i
    while k <=5:
        print(k,end=" ")
        k+=1



    print()
    i+=1

print()

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")

    for k in range(i,6):
        print(k,end=" ")
    


    print()