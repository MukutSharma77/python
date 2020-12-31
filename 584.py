'''Partially Hidden String
Create a function that takes a phrase and transforms each word using the following rules:
Keep first and last character the same.
Transform middle characters into a dash -.
Examples
partially_hide("skies were pretty") ➞ "s---s w--e p----y"
partially_hide("red is not my color") ➞ "r-d is n-t my c---r"
partially_hide("She rolled her eyes") ➞ "S-e r----d h-r e--s"
partially_hide("Harry went to fight the basilisk") ➞ "H---y w--t to f---t t-e b------k"
Notes
Words with two or fewer letters should not be hidden at all.'''

string="Harry went to fight the basilisk".split(' ')
print(string)

for i in range(len(string)):
    if string[i][0]:
        print(string[i][0] + '-' * (len(string[i])-2),end="")

    if string[i][-1]:
        print(string[i][-1],end=" ")

    else:
        print('-')
