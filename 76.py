'''Assuming that we have some email addresses in the "username@companyname.com" format,
 please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
john@google.com
Then, the output of the program should be:
google '''



#taking input
email=input("Enter Email :   ")

# Checking that email should not contain numeric value
for i in email:
    if i.isdigit():
        print("No digits should be there in Email")
    else:
        pass


#Running loop range starting from  index of @ + 1 and break at .
idx=email.index('@')
print("Company name :    ",end="  ")
for i in range(idx+1,len(email)):
    if email[i]=='.':
        break
    else:
        print(email[i],end="")
