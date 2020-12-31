'''Histogram Function
Build a function that creates histograms. Every bar needs to be on a new line and its length corresponds to the numbers in the list passed as an argument. The second argument of the function represents the character that needs to be used.
histogram(lst, char) -> str
Examples
histogram([1, 3, 4], "#") ➞ "#\n###\n####"
#
###
####
histogram([6, 2, 15, 3], "=") ➞ "======\n==\n===============\n==="
======
==
===============
==='''


lst=[6,12,15,3]
chr='='
for i in lst:
    print(chr*i)