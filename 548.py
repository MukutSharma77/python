'''Same ASCII?
Return True if the sum of ASCII values of the first string is same as the sum of ASCII values of the second string, otherwise return False.
Examples
same_ascii("a", "a") ➞ True
same_ascii("AA", "B@") ➞ True
same_ascii("EdAbIt", "EDABIT") ➞ False'''

string1="A"
string2= "A"
ascii1=0
for i in string1:
    ascii1+=ord(i)

ascii2=0
for i in string2:
    ascii2+=ord(i)

if ascii1==ascii2:
    print(True)
else:
    print(False)
