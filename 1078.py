'''Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
For example:
res = calculation(40, 10)
print(res)
A res should produce result (50, 30)'''

def calculation(num1,num2):
    return num1+num2 , num1-num2

res=calculation(40,10)
print(res)