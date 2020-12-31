'''Standard Deviation
The standard deviation is calculated following five steps:
Obtain the mean of the data set.
For each value in the set calculate the absolute difference between the value and the mean.
Square each value obtained and sum them cumulatively.
Divide the result by the data set length.
Get the square root of the value obtained.
Given a list of values return the standard deviation rounded to the nearest hundredth.
Examples
standard_deviation([3, 5, 7]) ➞ 1.63
// |(3-5)|+|(5-5)|+|(7-5)| = 2² + 0 + 2² = 8 / 3 = square root of 2.66 = 1.63
standard_deviation([5, 5, 5]) ➞ 0
// Values aren't deviating from the mean.
standard_deviation([-3, -5, -7]) ➞ 1.63
// Remember: absolute differences!'''

# list
lst=[-3,-5,-7]

#Finding mean
mean=sum(lst)/len(lst)

#For each value in the set calculate the absolute difference between the value and the mean.
lst2=[abs(i-mean) for i in lst]
print(lst2)

#Square each value obtained and sum them cumulatively
lst_sq=[i**2 for i in lst2]
print(lst_sq)

'''Divide the result by the data set length.
Get the square root of the value obtained.
'''
import  math
print(round(math.sqrt(sum(lst_sq)/len(lst_sq)),2))