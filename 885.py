'''
1
2 3 4
5 6 7 8 9
'''

i=1
k=1
while i<=5:
    j=0
    while j<i:
        print(k,end=" ")
        k+=1
        j+=1
    print()
    i+=2

print()
k=1
for i in range(1,6,2):
    for j in  range(0,i):
        print(k,end=" ")
        k+=1
    print()