'''Assuming that we have some email addresses in the "username@companyname.com" format,
 please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
john@google.com
Then, the output of the program should be:
john '''

#taking input
email=input("Enter Email :   ")

# Checking that email should not contain numeric value
for i in email:
    if i.isdigit():
        print("No digits should be there in Email")
    else:
        pass

#Printing name from email and if i= '@' than  break
print("Name is :   ",end="  ")
for i in email:
    if i == '@':
        break
    else:
        print(i,end="")
