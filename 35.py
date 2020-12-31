#Two Strings are Anagrams

#Inputting two string
str1=input("Enter String1 :   ")
str2=input("Enter String2 :   ")

#Comparing sorted two string to checking anagram or not

if sorted(str1) == sorted(str2):
    print("Yes String is anagram")
else:
    print("Not a anagram")

