#Create a function that takes a string and returns a string with its letters in alphabetical order.

#Inputting string and sorting it

string_=input("Enter String :   ")

#Checking is each eleement is alphabet or not
count=0
for i in string_:
    if i.isalpha():
        count+=1
    else:
        pass


string_=sorted(string_)
string_=('').join(string_)
if count==len(string_):
    print("The string in alphabetic order :   ",string_)
else:
    print("String include digit\INVALID")