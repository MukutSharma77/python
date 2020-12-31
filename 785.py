'''Harmonic Series
In mathematics, the harmonic series is the divergent infinite series:
Alternative Text
Its name derives from the concept of overtones, or harmonics in music.
Create a function that, given a precision parameter, returns the value of the harmonic series.
Examples
harmonic(3) ➞ 1.833
harmonic(1) ➞ 1.0
harmonic(5) ➞ 2.283
Notes
Round the result to the third decimal place.'''

num=5
if num>0:
    lst=[1/i for i in range(1,num+1)]

print(round(sum(lst),3))