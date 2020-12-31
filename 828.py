'''All About Lambda Expressions: Adding
Write a function that returns a lambda expression, which adds n to its input
Examples
adds1 = adds_n(1)
adds1(3) ➞ 4
adds1(5.7) ➞ 6.7
adds10 = adds_n(10)
adds10(44) ➞ 54
adds10(20) ➞ 30'''


adds1= lambda n : n+1
adds10= lambda n : n+10



output=adds1(3)
print(output)
output=adds1(5.7)
print(output)
output=adds10(44)
print(output)
output=adds10(20)
print(output)