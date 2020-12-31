'''The pH Scale
Given a pH value, return whether that value is "alkaline" (greater than 7), "acidic" (less than 7), or "neutral" (7). Return "invalid" if the value given is less than 0 or greater than 14.
Image of a pH chart
Examples
pH_name(5) ➞ "acidic"'''

num=int(input("pH Number :    "))
if num < 7 and num > 0:
    print('acidic')
elif num == 7:
    print('neutral')
else:
    print('alkaline')