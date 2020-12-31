'''Lemonade Stand
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Return True if and only if you can provide every customer with correct change.
Examples
lemonade([5, 5, 5, 10, 20]) ➞ True
lemonade([5, 5, 10, 10, 20]) ➞ False
lemonade([10, 10]) ➞ False
lemonade([5, 5, 10]) ➞ True'''

def lemonade(lst):
    five=0
    other=0
    for i in lst:
        if i==5:
            five+=5
        else:
            other+=i

    print(other-five<=five)


lemonade([5, 5, 5, 10, 20])
lemonade([5, 5, 10, 10, 20])
lemonade([10, 10])
lemonade([5, 5, 10])