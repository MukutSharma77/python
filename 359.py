'''Create a function which returns the type of triangle, given the side lengths. Return the following values if they match the criteria.
No sides equal: "scalene"
Two sides equal: "isosceles"
All sides equal: "equilateral"
Less or more than 3 sides given: "not a triangle"
Examples
get_triangle_type([2, 6, 5]) ➞ "scalene"
get_triangle_type([4, 4, 7]) ➞ "isosceles"
get_triangle_type([8, 8, 8]) ➞ "equilateral"
get_triangle_type([3, 5, 5, 2]) ➞ "not a triangle"'''

def get_triangle_type(triangle):
    if len(triangle)==3:
        if len(triangle)==triangle.count(triangle[0]):
            print("Equilateral")

        elif triangle.count(triangle[0])==2 or triangle.count(triangle[-1])==2:
            print('isosceles')

        else:
            print('Scalene')
    else:
        print('Not a triangle')


triangle=[6,5,8]
get_triangle_type(triangle)