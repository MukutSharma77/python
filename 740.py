'''Remove Repeated Characters
Create a function that will remove any repeated charcter(s) in a word passed to the function. Not just consecutive characters, but characters repeating anywhere in the input.
Examples
unrepeated("hello") ➞ "helo"
unrepeated("aaaaa") ➞ "a"
unrepeated("WWE!!!") ➞ "WE!"
unrepeated("call 911") ➞ "cal 91"'''


string="aaaaaaaaaa"
str_= ''
for i in string:
    if i not  in str_:
        str_+=i
print(str_)