#Palindromic Dates?

print("ex : 21/22/2020")
date=input("Enter Date :   ")

#Replacing slans to blank
date=date.replace("/","")

if date == date[::-1]:
    print("Yes date is palindrome")
else:
    print("No date is not a palindrome")