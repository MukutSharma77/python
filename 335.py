'''Count the Syllables
Create a function that returns the number of syllables in a simple string. The string is made up of short repeated words like "Lalalalalalala" (which would have 7 syllables).
Examples
count_syllables("Hehehehehehe") ➞ 6
count_syllables("bobobobobobobobo") ➞ 8'''

def count_syllabus(string):
    print(string.count(string[:2]))


string='Hehehehehehe'.lower()
count_syllabus(string)
