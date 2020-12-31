'''Volume of a Box
Create a function that takes a dictionary argument sizes (contains width, length, height keys) and returns the volume of the box.
Examples
volume_of_box({ "width": 2, "length": 5, "height": 1 }) ➞ 10
volume_of_box({ "width": 4, "length": 2, "height": 2 }) ➞ 16'''


dict_={ "width": 2, "length": 5, "height": 1 }

product=1
for i in dict_.values():
    product*=i

print(product)