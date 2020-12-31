#Print product of n number

num=int(input("Enter Number :   "))
tot=1
for i in range(1,num+1):
    tot*=i

print(tot)