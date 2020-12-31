''' Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it'''

def outer_funct(num1,num2):
    def inner_func(num1, num2):
        tot=num1+num2
        return tot

    sol=inner_func(num1,num2)
    return sol+5

ans=outer_funct(5,5)
print(ans)