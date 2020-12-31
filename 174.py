'''174)		You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
Return the total profit made, rounded to the nearest dollar.
Examples
profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796
'''

#Inputtinmg a dictionary
profit={
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}

#printing cp sp inverntory
print("The cost price is :   ",profit['cost_price'])
print("The sell price is :   ",profit['sell_price'])
print("The inventory is :   ",profit['inventory'])

print()
profit_= (profit['sell_price'] * profit['inventory'])  -  profit['cost_price'] * profit['inventory']
print("The profit is   :    ",profit_)