'''Squares and Cubes
Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.
Examples
check_square_and_cube([4, 8]) ➞ True
check_square_and_cube([16, 48]) ➞ False
check_square_and_cube([9, 27]) ➞ True'''

def check_square_and_cube(lst):
    c=0
    for i in range(1,lst[0]):
        if i**2==lst[0] and i**3==lst[1]:
            print(True)
            print(i)
            c+=1
            break
    if c==0:
        print(False)
check_square_and_cube([4, 8])
check_square_and_cube([16, 48])
check_square_and_cube([9, 27])