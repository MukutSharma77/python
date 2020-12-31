'''
enter String : MUKUT
M
M U
M U K
M U K U
M U K U T
'''
string=input('enter String : ')
i=1
while i<=len(string):
    j=0
    while j<i:
        print(string[j],end=" ")
        j+=1
    print()
    i+=1

print()

for i in range(1,len(string)+1):
    j=0
    for j in range(0,i):
        print(string[j],end=" ")
    print()