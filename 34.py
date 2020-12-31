#Remove the nth Index Character from a Non-Empty String

#inputing string and Nth character
string = input("Enter String :   ")
nth = int(input("Remove Nth index chacter from index :    "))

#First checking is given index is in the length of string if yes removing it
if nth <= len(string):
    string=string.replace(string[nth],"")

    print("After Remving :   ",string)
else:
    print("Something wrong")
