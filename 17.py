#Read a Number n and Print the Natural Numbers Summation Pattern

#Inputing number
num=int(input("Enter Number :   "))

#using two loops here to pring 1 =1 1 + 2 =3 till 1+...+n=Total

for i in range(1,num+1):
    tot=0
    for j in  range(1,i+1):
        tot+=j
        print(j,end=" ")
        if j==i:
            print(" = ",end=" ")
        else:
            print(" + ",end=" ")
    print(tot)