'''
A
A  B
A   B  C
A  B  C  D
A  B  C  D  E'''

#assinging  asci value to j and converting it in charcter with chr()
for i in range(65,70):
    j=65
    for j in range(65,i+1):
        print(chr(j),end="  ")
    print()