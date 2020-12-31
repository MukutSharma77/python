'''
Enter number :   7
      A
     B C
    D E F
   G H I J
  K L M N O
 P Q R S T U
V W X Y Z [ \
'''


n=int(input('Enter number :   '))
ascii_num=65

i=1
while i <= n:
    space=n-i
    while space>=1:
        print(' ',end="")
        space-=1
    j=1
    while j<=i:
        print(chr(ascii_num),end=" ")
        j+=1
        ascii_num+=1
    print()
    i+=1


n=7
ascii_num=65

for i in range(1,n+1):
    for space in range(7-i,0,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(ascii_num),end=" ")
        ascii_num+=1
    print()