'''Write a Python program to convert a string to a list.
color ="['Red', 'Green', 'White']"
Output :
['Red', 'Green', 'White']'''

color ="['Red', 'Green', 'White']"
color=color.strip('"[]"')
color=color.split(',')
print(color)
output=[]
for i in color:
    i=i.strip(" ")
    i=i.strip("''")
    output.append(i)
print(output)
