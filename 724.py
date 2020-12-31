'''Stretched Words
Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.
Examples
unstretch("ppoeemm") ➞ "poem"
unstretch("wiiiinnnnd") ➞ "wind"
unstretch("ttiiitllleeee") ➞ "title"
unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"
Notes
Final strings won't include words with double letters (e.g. "passing", "lottery").'''

string="wiiiinnnnd"

str2=''
for i in string:
    if i not in str2:
        str2+=i
print(str2)