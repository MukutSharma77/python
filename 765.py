'''Letters Only
Check if the given string consists of only letters and spaces and if every letter is in lower case.
Examples
letters_only("PYTHON") ➞ False
letters_only("python") ➞ True
letters_only("12321313") ➞ False
letters_only("i have spaces") ➞ True
letters_only("i have numbers(1-10)") ➞ False
letters_only("") ➞ False'''

string="PYTHON"
print( ' ' in string or string.isalpha() and string.islower() )