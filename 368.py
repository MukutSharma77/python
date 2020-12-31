'''Triangle and Parallelogram Area Finder
Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.
Examples
area_shape(2, 3, "triangle") ➞ 3
area_shape(8, 6, "parallelogram") ➞ 48
area_shape(2.9, 1.3, "parallelogram") ➞ 3.77'''

def area_shape(base,hieght,shape):
    if shape=='triangle':
        print((1/2) * base * hieght )
    elif shape=='parallelogram':
        print(base*hieght)
    else:
        print("Invalid Shape")

        



base=float(input("Enter Base :  "))
hieght=float(input("Enter Hieght :  "))
shape=input("Shape :  ").lower()
area_shape(base,hieght,shape)
