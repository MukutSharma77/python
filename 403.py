'''
Create a function that takes a list of strings and returns the words that are exactly four letters.
Examples
is_four_letters(["Tomato", "Potato", "Pair"]) ➞ ["Pair"]
is_four_letters(["Kangaroo", "Bear", "Fox"]) ➞ ["Bear"]
is_four_letters(["Ryan", "Kieran", "Jason", "Matt"]) ➞ ["Ryan", "Matt"]'''


list_=["Ryan", "Kieran", "Jason", "Matt"]
list_2=[]
for i in list_:
    if len(i)==4:
        list_2.append(i)

if list_2:
    print(list_2)
else:
    print('NONE')