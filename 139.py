#Create a function to return the absolute the given value in Python


#If the number is less than -1 thn muliplying it by -1 to make it positive
def absolute(num):
    if num <= -1:
        print("Number :    ",num*(-1))
    else:
        print("Number is already absolute :   ",num)



#Inputting number and calling a function
num=float(input("Enter number :    "))
absolute(num)