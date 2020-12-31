''' Generate a Python list of all the even numbers between 4 to 30
fuct_create(4,30)
Expected Output:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]'''


def fuct_create(num1,num2):
    lst=[i for i in range(num1,num2) if i % 2==0]
    return lst

sol=fuct_create(4,30)
print(sol)