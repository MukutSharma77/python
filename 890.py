'''
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
0 5 10 15 20 25
0 6 12 18 24 30 36
'''

i=0
while i<=6:
    k=0
    j=0
    while j<=i:
        print(k,end=" ")
        k+=i
        j+=1
    print()
    i+=1

print()

for i in range(0,7):
    k=0
    for j in range(i+1):
        print(k,end=" ")
        k+=i
    print()