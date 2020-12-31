# Design a simple calculator using if elif (just like switch case)

#Inputting two number and printing Operationg
num1=float(input("Enter Number 1 :   "))
num2=float(input("Enter Number 2 :   "))
print()
print("1) ADD\t 2 ) Subtract\t 3) Multiplication\t  4 ) Divide")
print()
choose=int(input("Choose any one :   "))

# Condition now

if choose==1:
    print("Addition of two number is :   ",num1+num2)
elif choose==2:
    print("Subtraction of two number is :   ",num1-num2)

elif choose==3:
    print("Multiplication of two number is :   ",num1*num2)


elif choose==4:
    print("Divsion of two number is :   ",num1/num2)

else:
    print("Invalid choose")