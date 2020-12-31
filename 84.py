#Python Program to Check if a Given Key Exists in a Dictionary or Not

#Craeting a dictionary
dictionary1={
    'Name' : 'Mukut',
    'Last_name' : 'Sharma',
    'Gender' : 'Male',
    'Birthdate' : '20/02/2000'
}

#Inputting key for searh..Searching with the help of loop
key_=input("Kwy exist in dictionary :  ")

if key_ in dictionary1:
    print("Yes it is present \n The value is :   ",end=" ")
    print(dictionary1.get(key_))
else:
    print("Not present")