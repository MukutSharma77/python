'''Index Shuffle
Write a function that takes all even-indexed characters and odd-indexed characters from a string and concatenates them together.
To illustrate:
index_shuffle("abcd") ➞ "acbd"
// "ac" (even-indexed) + "bd" (odd-indexed)
Examples
index_shuffle("abcdefg") ➞ "acegbdf"
index_shuffle("holiday") ➞ "hldyoia"
index_shuffle("maybe") ➞ "myeab"
'''

string='holiday'
string_ev=''
string_od=''
for i in string:
    if string.index(i) % 2==0:
        string_ev+=i
    else:
        string_od+=i

print(string_ev+string_od)