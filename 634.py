'''Hamming Distance
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"
Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1
Notes
Both strings will have the same length.'''

string1='strong'
string2='strung'
count=0

if len(string1)==len(string2):
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            count+=1

print(count)