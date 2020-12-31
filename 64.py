#)Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

#inputting string converting it in lower case
string=input("Enter String Yes or No  ?  :   ").lower()


#Condition If strng is yes than output : Yes else : NO
if string=='yes':
    print("Yes")

else:
    print("No")
