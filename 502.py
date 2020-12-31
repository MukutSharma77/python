'''Western Showdown
Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot) his gun faster than his opponent in a gun standoff.
Given two strings,p1 and p2, return which person drew their gun the fastest. If both are drawn at the same time, return "tie".
Examples
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"
# p1 draws his gun sooner than p2
showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"'''

string1="       Bang!         "
string2="       Bang!         "

string1=string1.rstrip()
string2=string2.rstrip()

if string1.count(" ")>string2.count(" "):
    print('p2')

elif string1.count(" ")<string2.count(" "):
    print('p1')

else:
    print('tie')