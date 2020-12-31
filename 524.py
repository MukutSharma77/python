'''Superheroes
Create a function that takes a list of names of superheroes and superheroines and returns a list of only the names of superheroes ending in "man" in alphabetical order.
Examples
superheroes(["Batman", "Superman", "Spider-man", "Hulk", "Wolverine", "Wonder-Woman"])
➞ ["Batman", "Spider-man", "Superman"]
superheroes(["Catwoman", "Deadpool", "Dr.Strange", "Captain-America", "Aquaman", "Hawkeye"])
➞ ["Aquaman"]
superheroes(["Wonder-Woman", "Catwoman", "Invisible-Woman"])
➞ []'''

lst=["Batman", "Superman", "Spider-man", "Hulk", "Wolverine", "Wonder-Woman"]

lst2=[]
for i in lst:
    if i[-3:]=='man' and i[-5:]!='Woman':
        lst2.append(i)

print(lst2)