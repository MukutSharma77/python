#Read a Number n And Print the Series "1+2+…..+n= "

#input number
num=int(input("Enter number :  "))

#using loop to display 1 + 2 ....+n = TOTAL
tot=0
for i in range(1,num+1):
    tot+=i
    print(i,end=" ")
    if i == num:
        print(f' = {tot} ')
    else:
        print("+",end=" ")
