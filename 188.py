#convert bin. to dec

binary=int(input("Enter binary number :    "))
string=''

#checking whether input number is binary or not
for i in str(binary):
    if i=='0' or i =='1':
        string+=i
    else:
        pass


if string==str(binary):
    tot=0
    binary=str(binary)
    j=len(binary) - 1
    for i in range(0,len(binary)):
        if binary[i]=='1':
            tot+= (2 ** j)
        j-=1
    print(tot)


else:
    print("Not a binary")
