#Create a function that returns the ASCII value of the passed in character.

#inputting string
string_=input("Enter string to know ascii value :   ")

#Checking is len of string is 1 if yes than print ascii value
if len(string_)==1:
    print("The ascii value is :  ",ord(string_))
else:
    print("Invalid")