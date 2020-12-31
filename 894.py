'''
A
B B
C C C
D D D D
E E E E E

'''

i=1
alpha=65
while i<=5:
    j=1
    while j<= i:
        print(chr(alpha),end=" ")
        j+=1
    print()
    alpha+=1
    i+=1

print()

alpha=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(alpha),end=" ")
    alpha+=1
    print()