#Write a Python program to test whether a passed letter is a vowel or not.

character=input("Enter Charcter :   ").lower()

if len(character) == 1:
    if character=='a' or character=='e' or character=='i' or character=='u' or character=='o':
        print("The given chrcter is vowel")
    else:
        print("Consonent")

else:
    print("Invalid input")