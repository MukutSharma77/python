'''Lists, written with [] square brackets, such as [1, 2, 4, 8].
Tuples, written with () parenthesis, such as (7, 8, 9).
Sets, written with{} curly brackets, such as {2, 3, 5, 7, 11, 13}.
Each of these types has its own special properties and peculiarities that are worth knowing, but this challenge is only about transforming these data types into each other.
This can be done as in the following:
tuple([1,2,4,8]) returns (1,2,4,8)
list({2,3,5,7,11}) returns [2, 3, 5, 7, 11, 13]
set((1,2,4)) returns {1,2,4}'''


list_=[1,2,3,4,5]
change=input("Change type :  ").lower()

if change=='list':
    print(list(list_))

elif change=='tuple':
    print(tuple(list_))


elif change=='set':
    print(set(list_))

else:
    print("Invalid")