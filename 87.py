#Python Program to Remove the Given Key from a Dictionary


#Craeting a dictionary
dictionary1={
    'Name' : 'Mukut',
    'Last_name' : 'Sharma',
    'Gender' : 'Male',
    'Birthdate' : '20/02/2000'
}

#inputting key Checking wheather input key is in dict or not

key_=input("Delete key from dict :     ")

if key_ in dictionary1:
    dictionary1.pop(key_)
    print(dictionary1)
else:
    print("Not present")