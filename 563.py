'''Removing Enemies
Remove enemies from the list of people, even if the enemy shows up twice.
Examples
remove_enemies(["Fred"], []) ➞ ["Fred"]
remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]) ➞ ["Adam", "Tanya"]
remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]) ➞ ["Emily", "Steve"]'''

lst1=["John", "Emily", "Steve", "Sam"]
lst2=["Sam", "John"]

lst3=[]
for i in lst1:
    if i not in lst2:
        lst3.append(i)
    else:
        pass

print(lst3)