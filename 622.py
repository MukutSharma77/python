'''Is the Number Even or Odd?
Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
Examples
isEvenOrOdd(3) ➞ "odd"
isEvenOrOdd(146) ➞ "even"
isEvenOrOdd(19) ➞ "odd"'''

num=19
msg='even' if num%2==0 else 'odd'
print(msg)