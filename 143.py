'''calculate discount based on the amount and given discount rate
 Amount          Discount
    0-5000          5%
    5000-15000      12%
    15000-25000     20%
    above 25000     30%'''

amount=int(input("Enter Amount :   "))

if amount > 0:
    if amount <= 5000:
        dis=amount * (5 / 100)
        amount=amount-dis
    elif amount <= 15000:
        dis=amount * 12 /100
        amount=amount-dis
    elif amount <= 25000:
        dis=amount * 20 /100
        amount=amount-dis
    else:
        dis=amount * 30 /100
        amount=amount-dis

    print("Discount :   ",dis)
    print("Amount after discount :  ",amount)


else:
    print("Amount can not be negative  and equal to zero")


