'''Find the Discount
Create a function that takes two arguments: the final price and the discount as integers and returns the final price after the discount.
Alternative Text
Examples
dis(1500, 50) ➞ 750
dis(89, 20) ➞ 71.2
dis(100, 75) ➞ 25'''


def dis(final_price,discount):
    out=final_price - (final_price * discount/100)
    if int(out)==out:
        print(int(out))
    else:
        print(out)

dis(1500, 50)
dis(89, 20)
dis(100, 75)
