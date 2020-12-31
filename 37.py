#Counting vowel from a given string

#inputting a String
string=input("Enter String :    ")
print("Given String is :   ",string)
string=string.lower()
count=0
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' in string:
        count+=1

    else:
        pass

if count > 0:
    print('Total vowel is : ',count)
else:
    print("No Vowel in a given string")