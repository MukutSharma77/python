'''Write a python program that displays a message as follows for a given number:
If it is a multiple of three, display "Zip".
If it is a multiple of five, display "Zap".
If it is a multiple of both three and five, display "Zoom".
If it does not satisfy any of the above given conditions, display "Invalid".'''


#Inputting number
num=int(input("Enter number :  "))

if num % 3==0 and num % 5 ==0:
    print("Zoom")
elif num % 3==0:
    print("zip")
elif num % 5==0:
    print("Zap")
else:
    print("Invalid")