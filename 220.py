'''Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

num1=int(input("Enter Number1 :   "))
num2=int(input("Enter Number2 :   "))

if num2==num1 or num2+num1==5 or num1 - num2==5:
    print(True)
else:
    print(False)