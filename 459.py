'''Hashes and Pluses
Create a function that returns the number of hashes and pluses in a string.
Examples
hash_plus_count("###+") ➞ [3, 1]
hash_plus_count("##+++#") ➞ [3, 3]
hash_plus_count("#+++#+#++#") ➞ [4, 6]
hash_plus_count("") ➞ [0, 0]'''

string=''
list_=[string.count('#'),string.count('+')]
print(list_)