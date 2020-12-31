'''Print A to Z except vowel with While Loop'''

i=65
for i in range(65,91):
    if chr(i) in 'AEIOU':
        continue
    else:
        print(chr(i),end="  ")
