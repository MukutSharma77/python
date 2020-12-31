'''
A B C D E
  A B C D
    A B C
      A B
        A
'''

i=5
while i>=1:
    ascii_num=65
    space=5-i
    while space>=1:
        print(' ',end=" ")
        space-=1
    j=1
    while j<=i:
        print(chr(ascii_num),end=" ")
        ascii_num+=1
        j+=1
    print()
    i-=1


for i in range(5,0,-1):
    for space in range(5-i,0,-1):
        print(' ',end=" ")
    ascii_num=65
    for j in range(1,i+1):
        print(chr(ascii_num),end=" ")
        ascii_num+=1
    print()