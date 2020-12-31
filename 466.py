'''Program to calculate Electricity Bill
1 to 100 units – Rs. 10/unit
100 to 200 units – Rs. 15/unit
200 to 300 units – Rs. 20/unit
above 300 units – Rs. 25/unit'''

unit=int(input("Enter Total Unit :   "))

result=0
if unit <= 100:
    result=unit*10

elif unit <= 200:
    result=(100*10) + (unit-100)*15

elif unit <= 300:
    result=((100 * 10) + (100*15)) + ((unit-200) * 20)

else:
    result=((100 * 10) + (100 * 15) + (100 * 20)) + ((unit - 300) * 25)

print(result)