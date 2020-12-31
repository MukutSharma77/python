#calculate the number of upper case letters and lower case letters.

#inputting string

string=input("Enter String :   ")


upper=0
lower=0

#Counting Upper case and lower case
for i in  string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        pass


#printing

print("Total upper case letter is :  ",upper)

print("Total lower case letter is :  ",lower)