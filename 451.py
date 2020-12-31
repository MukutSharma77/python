'''Is Sam with Frodo?
Sam and Frodo need to be close. If they are side by side in the list, your function should return True. If there is a name between them, return False.
Examples
middle_earth(["Frodo", "Sam", "Gandalf"]) ➞ True
middle_earth(["Frodo", "Saruman", "Sam"]) ➞ False
middle_earth(["Orc", "Sam", "Frodo", "Legolas"]) ➞ True'''

list_=["Frodo", "Saruman", "Sam"]
print(abs(list_.index('Sam')-list_.index('Frodo'))==1)