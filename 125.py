#Python Program to Find the LCM of Two Numbers

num1=int(input("Enter Number1 : "))
num2=int(input("Enter Number2 : "))
tot=1

if num1>num2:
    greater=num1
else:
    greater = num2


while True:
    if greater % num1==0 and greater % num2==0:
        lcm=greater
        break
    greater+=1

print(lcm)
