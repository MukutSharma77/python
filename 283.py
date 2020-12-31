'''
Create a function that takes a string and returns the first character of every word if the length of the word is even and the middle character if the length of the word is odd.
Examples
stmid("Alexa have to paid") ➞ "ehtp"
# "e" is the middle character of "Alexa"
# "h" is the first character of "have"
'''


string="Alexa have to paid".split(' ')


for i in string:
   if len(i) % 2==0:
        print(i[0],end="    ")
   else:
        print(i[len(string)//2], end="    ")
