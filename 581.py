'''Position in the Alphabet
Given a number between 1-26, return what letter is at that position in the alphabet. Return "invalid" if the number given is not within that range, or isn't an integer.
Examples
letter_at_position(1) ➞ "a"
letter_at_position(26.0) ➞ "z"
letter_at_position(0) ➞ "invalid"
letter_at_position(4.5) ➞ "invalid"
'''

try:
    num=input("Enter Number :   ")
    if int(num)>0 and int(num)<=26:
        print(chr(97+int(num)-1))

except Exception as e:
    print('Inavlid')