'''Online Shopping
Create a function that determines whether a shopping order is eligible for free shipping. An order is eligible for free shipping if the total cost of items purchased exceeds $50.00.
Examples
free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 }) ➞ False
free_shipping({ "Flatscreen TV": 399.99 }) ➞ True
free_shipping({ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }) ➞ True'''


dict_={ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }
tot=0
for i in dict_.values():
    tot+=i

if tot >= 50:
    print(True)
else:
    print(False)