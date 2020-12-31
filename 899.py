'''
     A
    A B
   A B C
  A B C D
 A B C D E
A B C D E F
 G H I J K
  L M N O
   P Q R
    S T
     U
'''
i=1
while i<=6:
    space=6-i
    ascii_num=65
    while space>=1:
        print(' ',end="")
        space-=1
    j=1
    while j<=i:
        print(chr(ascii_num),end=" ")
        ascii_num+=1
        j+=1
    print()
    i+=1

ascii_num=71
i=5
while i >= 1:
    space=6-i
    while space>=1:
        print(' ',end="")
        space-=1
    j=1
    while j<=i:
        print(chr(ascii_num),end=" ")
        ascii_num+=1
        j+=1
    print()
    i-=1


print()
print()


for i in range(1,7):
    ascii_num = 65

    for space in range(7-i,0,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(ascii_num),end=" ")
        ascii_num+=1
    print()

ascii_num=71
for i in range(5,0,-1):
    for space in range(7-i,0,-1):
        print(' ',end="")
    for j in range(i,0,-1):
        print(chr(ascii_num),end=" ")
        ascii_num+=1
    print()