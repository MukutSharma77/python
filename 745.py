'''Percentage Changed
Create a function that takes an old price old, a new price new, and returns what percent the price decreased or increased. Round the percentage to the nearest whole percent.
Examples
percentage_changed("$800", "$600") ➞ "25% decrease"
percentage_changed("$1000", "$840") ➞ "16% decrease"
percentage_changed("$100", "$950") ➞ "850% increase"
'''
'''[(New Price - Old Price)/Old Price] and then multiply that number by 100. If the price decreased,
 use the formula [(Old Price - New Price)/Old Price] and multiply that number by 100.'''
price1='$100'
price2='$950'

old_price=int(price1[1:])
new_price=int(price2[1:])
# print(new_price,old_price)
if new_price > old_price:
    dis=(new_price-old_price)/old_price
    print(str(round(dis*100))+'% increase')

else:
    dis = (old_price - new_price) / old_price
    print(str(round(dis*100))+'% decrese')
