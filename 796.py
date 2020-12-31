'''Explosion Intensity
Given a number, return a string of the word "Boom", which varies in the following ways:
The string should include n number of "o"s, unless n is below 2 (in that case, return "boom").
If n is evenly divisible by 2, add an exclamation mark to the end.
If n is evenly divisible by 5, return the string in ALL CAPS.
The example below should help clarify these instructions.
Examples
boom_intensity(4) ➞ "Boooom!"
# There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
boom_intensity(1) ➞ "boom"
# 1 is lower than 2, so we return "boom"
boom_intensity(5) ➞ "BOOOOOM"
# There are 5 "o"s and 5 is divisible by 5 (all caps)
boom_intensity(10) ➞ "BOOOOOOOOOOM!"
'''

def boom_intensity(n):
    if n < 2:
        print('boom')

    elif n%2==0:
        print('B' + 'O' * n + 'M!')

    elif n%5==0:
        print('B' + 'O' * n + 'M')

boom_intensity(4)
boom_intensity(1)
boom_intensity(5)
boom_intensity(10)
