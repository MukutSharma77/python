'''Both Zero, Negative or Positive
Write a function that returns True if both numbers are:
Smaller than 0, OR ...
Greater than 0, OR ...
Exactly 0
Otherwise, return False.
'''

num1=int(input("Enter Number 1 :  "))
num2=int(input("Enter Number 2 :  "))

if num1==num2:
    print(True)
elif num1> 0 and num2 > 0:
    print(True)
elif num1 <0 and num2 < 0:
    print(True)
else:
    print(False)