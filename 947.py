'''Write a Python program to split a list into different variables.
color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
print(var1)
print(var2)
print(var3)
Sample Output:
('Black', '#000000', 'rgb(0, 0, 0)')
('Red', '#FF0000', 'rgb(255, 0, 0)')
('Yellow', '#FFFF00', 'rgb(255, 255, 0)')
'''

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

a,b,c=color
print(a,'\n',b,'\n',c)