'''Temperature Conversion
Write a program that takes temperature input in Celsius and returns temperature measurements , after conversion to Fahrenheit and Kelvin.
The formula to calculate the temperature in Fahrenheit from Celsius is:
F = C*9/5 +32
The formula to calculate the temperature in Kelvin from Celsius is:
K = C + 273.15
Examples
tempConversion(0) ➞ [32, 273.15]
// 0°C is equal to 32°F and 273.15 K.
tempConversion(100) ➞ [212, 373.15]
tempConversion(-10) ➞ [14, 263.15]
tempConversion(300.4) ➞ [572.72, 573.55]
'''

num=-10
list_=[(num * 9/5) + 32 , (num+273.15)]
print(list_)