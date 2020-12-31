'''Simple OOP Calculator
Create methods for the Calculator class that can do the following:
Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.
Examples
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2'''

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 // self.num2

num1=10
num2=5
calculator = Calculator(num1,num2)
output=calculator.add()
print(output)
output=calculator.subtract()
print(output)
output=calculator.multiply()
print(output)
output=calculator.divide()
print(output)