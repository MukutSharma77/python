# sentence and calculate the number of letters and digits.

#inputting string
string=input("Enter string :   ")

#Finding number of digit and letter
alpha=0
num=0
for i in string:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        num+=1


#printing the number of letter and number

print("Total  number of Digit is :  ",num)

print("The number of Letters is :  ",alpha)