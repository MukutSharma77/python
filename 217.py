# Write a Python program to compute the greatest common divisor (GCD) of two positive integers

num1=int(input("Enter Number1 :   "))
num2=int(input("Enter Number2 :   "))
gcd=0
if num1 >= num2:
    for i in range(1,num1+1):
        if num1 % i ==0 and num2 % i == 0:
            gcd=i
        else:
            pass

else:
    for i in range(1, num2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        else:
            pass

print(gcd)