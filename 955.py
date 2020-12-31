''' Write a Python program to compute the difference between two lists
Color1=["red", "orange", "green", "blue", "white"]
color2= ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']'''


color1=["red", "orange", "green", "blue", "white"]
color2= ["black", "yellow", "green", "blue"]

color1_color2=[]
for i in color1:
    if i not in color2:
        color1_color2.append(i)
print('Color1 - Color2 =     ',color1_color2)

color2_color1=[]
for i in color2:
    if i not in color1:
        color2_color1.append(i)

print('Color2 - Color1 =    ',color2_color1)