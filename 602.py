'''Move Capital Letters to the Front
Examples
cap_to_front("hApPy") ➞ "APhpy"
cap_to_front("moveMENT") ➞ "MENTmove"
cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"
Notes
Keep the original relative order of the upper and lower case letters the same.
'''

string="hApPy"

upstr_=''
downstr=''

for i in string:
    if i.isupper():
        upstr_+=i
    else:
        downstr+=i

print(upstr_+downstr )