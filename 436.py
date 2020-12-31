'''Write a function that checks whether a person can watch an MA15+ rated movie. One of the following two conditions is required for admittance:
The person is at least 15 years old.
They have parental supervision.
The function accepts two parameters, age and is_supervised. Return a boolean.
Examples
accept_into_movie(14, True) ➞ True
accept_into_movie(14, False) ➞ False
accept_into_movie(16, False) ➞ True'''

age=19
boolean=False

if age>=15:
    print(True)
elif age<=14 and boolean==True:
    print(True)

else:
    print(False)