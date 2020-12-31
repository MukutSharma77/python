'''Shhh Be Quiet Function
Write a function that removes all capitals letters from a sentence except the first letter, put quotation marks around the sentence and add ", whispered Edabit." at the end.
Examples
shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'
shhh("tHaT'S Pretty awesOme") ➞ '"That's pretty awesome", whispered Edabit.'
shhh("") ➞ '"", whispered Edabit.'''

string="tHaT'S Pretty awesOme".capitalize()
print(f' \'"{string}",Whispered Edabit ')