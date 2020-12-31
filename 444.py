'''Little Dictionary
Create a function that takes an initial word and filters out a list which contains words that start with the same letters as the initial word.
Examples
dictionary("bu", ["button", "breakfast", "border"]) ➞ ["button"]
dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]) ➞ ["triplet", "tries", trip"]
dictionary("beau", ["pastry", "delicious", "name", "boring"]) ➞ []
'''

list_=["triplet", "tries", "trip", "piano", "tree"]
list2=[]
search='tri'
for i in list_:
    if i[:len(search)]==search:
        list2.append(i)

print(list2)