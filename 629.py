'''Inches to Feet
Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.
Examples
inches_to_feet(324) ➞ 27
inches_to_feet(12) ➞ 1
inches_to_feet(36) ➞ 3
Notes
If inches are under 12, return 0.'''

inch=36
feet=0 if inch < 12 else inch//12
print(feet)