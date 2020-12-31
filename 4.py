#Function for reversing and printing reverse number
def rev(num):
    print("\nYour Number is :   ",num)
    print("\nReversing a number :    ",end=" ")
    reverse_=0
    while num:
        module=num%10
        reverse_= (reverse_ * 10) + module
        num//=10

    print(reverse_)


#Inputting a number and calling a function
num= int(input("Enter Number  :    "))
rev(num)