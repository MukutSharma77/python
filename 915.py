'''
  M U K U T
    M U K U
      M U K
        M U
          M
'''

string='MUKUT'

i=len(string)-1
while i>=0:
    space=(len(string)-1)-i
    while space >= 1:
        print(' ',end=" ")
        space-=1
    j=0
    while j<=i:
        print(string[j],end=" ")
        j+=1
    print()
    i-=1
print()

for i in range(len(string)-1,-1,-1):
    for space in range(len(string)-1,i,-1):
        print(' ',end=" ")
    for j in range(0,i+1):
        print(string[j],end=" ")
    print()