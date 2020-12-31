#Write a function to compute 5/0 and use try/except to catch the exceptions

#Using try and except  as 5/0 will be an error : ZeroDivisionError: division by zero

try:
    num1=5
    num2=0
    tot=num1/num2

except Exception as e:
    print("0 in the dinominator not possible")
    print("Error :  ",e)