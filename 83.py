#Python Program to Concatenate Two Dictionaries Into One

dictionary1={
    'Name' : 'Mukut',
    'Last_name' : 'Sharma'
 }

dictionary2={
    'Gender' : 'Male',
    'Birthdate' : '20/02/2000'
}

dictionary1.update(dictionary2)
print(dictionary1)

