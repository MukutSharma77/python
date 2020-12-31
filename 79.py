'''Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Example:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']'''

#inputting string
string=input("Enter string :   ")

#Searching is there any digits in a number if yes appending in a list
list_=[]
for i in string:
    if i.isdigit():
       list_.append(i)

    else:
        pass

#Cheking element in listr or not
if list_:
    print(f"{list_}")
else:
    print("No digits in a string")