'''Counting Adverbs
Create a function that counts the number of adverbs in a sentence. An adverb is a word that ends with ly.
Examples
count_adverbs("She ran hurriedly towards the stadium.") ➞ 1
count_adverbs("She ate the lasagna heartily and noisily.") ➞ 2
count_adverbs("He hates potatoes.") ➞ 0
count_adverbs("He was happily, crazily, foolishly over the moon.") ➞ 3
'''

string="He was happily, crazily, foolishly over the moon.".split(' ')

count=0
for i in string:
    if 'ly' in i[-3:]:
        count+=1

print(count)