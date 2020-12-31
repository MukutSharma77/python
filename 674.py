'''Convert to Decimal Notation
Create a function to convert a list of percentages to their decimal equivalents.
Examples
convert_to_decimal(["1%", "2%", "3%"]) ➞ [0.01, 0.02, 0.03]
convert_to_decimal(["45%", "32%", "97%", "33%"]) ➞ [0.45, 0.32, 0.97, 0.33]
convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) ➞ [0.33, 0.981, 0.5644, 1]'''

lst=["33%", "98.1%", "56.44%", "100%"]
lst_=[]
for i in lst:
    i=float(i.replace('%',''))
    lst_.append(i)

lst_output=[]
for i in lst_:
    lst_output.append(i/100)

print(lst_output)