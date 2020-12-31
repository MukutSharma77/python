'''Remove Every Vowel from a String
Create a function that takes a string and returns a new string with all vowels removed.
Examples
remove_vowels("I have never seen a thin person drinking Diet Coke.")
➞ " hv nvr sn  thn prsn drnkng Dt Ck."
remove_vowels("We're gonna build a wall!")
➞ "W'r gnn bld  wll!"
remove_vowels("Happy Thanksgiving to all--even the haters and losers!")
➞ "Hppy Thnksgvng t ll--vn th htrs nd lsrs!"'''

string="I have never seen a thin person drinking Diet Coke."
str_=''
for i in string:
    if i=='a' or i=='e' or i=='i'or i=='o' or i=='u' or i=='A' or i=='E' or i=='I'or i=='O' or i=='U' :
        pass
    else:
        str_+=i

print(str_)