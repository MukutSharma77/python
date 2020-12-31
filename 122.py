#Create a function that returns True if the given string has any of the following:
# Only letters and no numbers.
# Only numbers and no letters.

#inputting string
string=input("Enter String ;   ")


#checking is all the element digit or alpha

count_digit=0
count_alpha=0
for i in string:
    if i.isalpha():
        count_alpha+=1
    elif i.isdigit():
        count_digit+=1
    else:
        pass


if count_digit==len(string) or count_alpha == len(string):
    print(True)
else:
    print(False)

