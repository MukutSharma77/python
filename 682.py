'''Compare by ASCII Codes
Create a function that compares two words based on the sum of their ASCII codes and returns the word with the smaller ASCII sum.
Examples
ascii_sort(["hey", "man"]) ➞ "man"
# ["h", "e", "y"] ➞ sum([104, 101, 121]) ➞ 326
# ["m", "a", "n"] ➞ sum([109, 97, 110]) ➞ 316
ascii_sort(["majorly", "then"]) ➞ "then"
ascii_sort(["victory", "careless"]) ➞ "victory"
Notes
Both words will have strictly different ASCII sums.'''

lst=['majority','then']

lst_0=[]
lst_1=[]
for i in lst[0]:
    lst_0.append(ord(i))

for i in lst[1]:
    lst_1.append(ord(i))

if sum(lst_0) > sum(lst_1):
    print(lst[1])
else:
    print(lst[0])