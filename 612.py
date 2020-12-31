'''Lexicographically First and Last
Write a function that returns the lexicographically first and lexicographically last rearrangements of a string. Output the results in the following manner:
first_and_last(string) ➞ [first, last]
xamples
first_and_last("marmite") ➞ ["aeimmrt", "trmmiea"]
first_and_last("bench") ➞ ["bcehn", "nhecb"]
first_and_last("scoop") ➞ ["coops", "spooc"]
'''

word="marmite"
lst=[''.join(sorted(word)) , ''.join(sorted(word,reverse=True))]
print(lst)