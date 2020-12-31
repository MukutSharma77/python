'''Image of Goooooooooogle
Let's say we wanted to change the number of pages that Google could skip to. Create a function where given a number of pages n, return the word "Google" but with the correct number of "o"s.
Examples
googlify(10) ➞ "Goooooooooogle"
googlify(23) ➞ "Gooooooooooooooooooooooooogle"
'''

num=int(input("Enter Number :  "))
print('G'+'o'*num+'gle')