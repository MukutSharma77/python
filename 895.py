'''
A
B C
D E F
G H I J
K L M N O
'''
i=1
alpha=65
while i<=5:
    j=1
    while j<=i:
        print(chr(alpha),end=" ")
        alpha+=1
        j+=1
    print()
    i+=1

print()
alpha=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(alpha),end=" ")
        alpha+=1
    print()