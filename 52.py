#Define a function that can accept two strings as input and print the string with maximum length in console.

#function to compare the length of two string
def length(str1,str2):
    if len(str1) > len(str2):
        print()
        print("The Length of string 1 is more    ")
        print("\n",str1)

    elif len(str2) > len(str1):
        print()
        print("The Length of string 2 is more    ")
        print("\n",str2)

    else:
        print("\nThe length of both the string is same ")
        print()
        print('String 1    :   '+str1)
        print()
        print('String 2    :   ' + str2)


#Inputing 2 string and than calling a function
str1=input("Enter string1  :   ")
str2=input("Enter string2  :   ")
length(str1,str2)