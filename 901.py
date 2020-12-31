string='MUKUT'
i=len(string)-1
while i>=0:
    j=i
    while j>=0:
        print(string[j],end=" ")
        j-=1
    print()
    i-=1

print()
for i in range(len(string)-1,-1,-1):
    for j in range(i,-1,-1):
        print(string[j],end=" ")
    print()