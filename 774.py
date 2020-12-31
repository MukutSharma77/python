'''In the Centre?
Given a string containing mostly spaces and one non-space character, return whether the character is positioned in the very centre of the string. This means the number of spaces on both sides should be the same.
Examples
is_central("  #  ") ➞ True
is_central(" 2    ") ➞ False
is_central("@") ➞ True'''

string="  #  "
print(string==string[::-1])