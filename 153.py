#convert a given decimal number to binary number

num=255

string=''
while num:
    if num % 2 == 0 or num % 2 == 1:
        string+=str(num%2)

    num//=2

print(string[::-1])
