'''A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12'''


#Inputting user_name and password

user_name=input("Enter User_name   :    ")
password=input("Enter Password     :    ")

count_upper=0
count_digit=0
count_lower=0
count_symbol=0

#Condititon for the length of a password
if len(password)>=6 and len(password)<=12:
    #Checkig is it right password contains all the condition
    for i in password:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1
        elif i.isdigit():
            count_digit+=1
        else:
            count_symbol+=1

    if count_digit == 0:
        print("Password Should contain atleast one digit")
    elif count_symbol == 0:
        print("Password Should contain atleast one Symbol")
    elif count_upper == 0:
        print("Password Should contain atleast one Upper case")
    elif count_lower==0:
        print("Password Should contain atleast one Lower case")
    else:
        print("Valid Password")

