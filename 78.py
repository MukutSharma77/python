# Please write a program which accepts a string from console and print it in reverse order.

#Inputting string using split() to store it in list form
string=input("Enter String :   ").split(" ")

#reversing the word first than charcters of a word
for i in string[::-1]:
    print(i[::-1],end=" ")