'''Find Unique Character Strings
Create a function that returns only strings with unique characters.
Examples
filter_unique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
# "b" occurs in "abb" more than once, "b" occurs in "abcdb" more than once, etc.
filter_unique(["88", "999", "989", "9988", "9898"]) ➞ []
filter_unique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]) ➞ ["ABCDE", "BED", "BAC"]'''

list_=["ABCDE", "DDEB", "BED", "CCA", "BAC"]

list_2=[i for i in  list_ if len(i)==len(set(i))]
print(list_2)