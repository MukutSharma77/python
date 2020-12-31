#whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically

#input string white space

string=input("Enter string :  ").split(" ")


#creating empty list than appending unique value
list_=[]

for i in string:
    if i  not in list_:
        list_.append(i)

#Sorting and printing list
list_=sorted(list_)
print((" ").join(list_))