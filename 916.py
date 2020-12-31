'''
M
U M
K U M
U K U M
T U K U M
'''

string='MUKUT'

i=0
while i<len(string):
    j=i
    while j>=0:
        print(string[j],end=" ")
        j-=1
    print()
    i+=1

print()

for i in range(0, len(string)):
    for j in range(i,-1,-1):
        print(string[j],end=" ")
    print()