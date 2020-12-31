#Write a Python program to concatenate all elements in a list into a string and return it.

list_=[1,2,3,'a',4.5,'7']
string=" "
print("List is  ",list_)

for i in list_:
    string+=str(i)

print("List in a string : ",string)