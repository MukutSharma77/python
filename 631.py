'''How Many Beans Has Joker Persona 5 Eaten?
Beans make Joker Persona 5 fart a lot. You can determine how hard he farts by how many beans he has eaten. The strength of the fart is equal to twice the square of the bean count plus 5 times the bean count, plus 3.
Create a function that takes an integer beans and return the fart power.
Examples
fart(3) ➞ 36
fart(0) ➞ 3
fart(6) ➞ 105
Notes
Make sure it's twice the square of the bean count, not the square of twice the bean count.
2* (beans**2) + 3 + 5*beans'''


bean=6
print(2 * (bean**2) + (5*bean) +3)